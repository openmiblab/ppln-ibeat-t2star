import os
import argparse
import logging

from tqdm import tqdm
import dbdicom as db
from utils.db_plot import db_mosaic


def run(build):

    input = 'stage_2_database'
    output = 'stage_3_check'

    results_dir = os.path.join(build, 't2star', output)
    os.makedirs(results_dir, exist_ok=True)
    summary = os.path.join(results_dir, 'summary.txt')

    for group in ['Controls', 'Patients']:
        database = os.path.join(build, 't2star', input, group) 
        csv = os.path.join(results_dir, f'{group}.csv')
        png_prefix = os.path.join(results_dir, f'{group}')
        params = {
            'EchoTime': os.path.join(results_dir, f'echo_time_{group}.txt'),
            'ImageType': os.path.join(results_dir, f'image_type_{group}.txt'),
        }
        run_db(database, csv, summary, png_prefix, params)


def run_db(database, csv, summary, png_prefix, params):
    _parameter_summary(database, params)
    db.to_csv(database, csv)
    _write_summary(database, summary)
    _build_mosaic(database, png_prefix, 'T2star_magn')
    _build_mosaic(database, png_prefix, 'T2star_phase')
    _build_mosaic(database, png_prefix, 'T2star_map_vendor', vmin=0, vmax=60)


def _build_mosaic(datapath, png_prefix, desc, vmin=None, vmax=None):

    png = f"{png_prefix}_{desc}.png"

    if os.path.exists(png):
        return

    series = db.series(datapath)
    series_desc = [s[-1][0] for s in series]
    series_t2star = [s for i, s in enumerate(series) if series_desc[i]==desc]

    db_mosaic(series_t2star, png, title=desc, vmin=vmin, vmax=vmax)


def _parameter_summary(clean_db, params):

    series = db.series(clean_db)
    for key in params:
        with open(params[key], 'a') as f:
            for s in tqdm(series, desc=f"Reading {key}.."):
                patient = s[1]
                study_desc = s[2][0]
                series_desc = s[3][0]
                vals = db.unique(key, s)
                prefix = f"{patient} > {study_desc} > {series_desc}"
                log_line = f"{prefix:<40}(n={len(vals):02d}): {vals}\n"
                f.write(log_line)


def _write_summary(datapath, summary):

    patients = db.patients(datapath)
    studies = db.studies(datapath)
    series = db.series(datapath)

    nr_studies = {}
    for patient in patients:
        n = len([s for s in studies if s[:2]==patient[:2]])
        if n in nr_studies:
            nr_studies[n] += 1
        else:
            nr_studies[n] = 1

    nr_series = {}
    for study in studies:
        n = len([s for s in series if s[:3]==study[:3]])
        if n in nr_series:
            nr_series[n] += 1
        else:
            nr_series[n] = 1

    with open(summary, 'a') as f:

        f.write('\n')
        # f.write(f"{group} ({'all sites' if site is None else site})\n")

        f.write('\n')
        f.write(f"  {len(patients)} patients with {len(studies)} studies\n")
        f.write('\n')
        for n in sorted(nr_studies.keys()):
            f.write(f"    {nr_studies[n]} with {n} studies\n")

        f.write('\n')
        f.write(f"  {len(studies)} studies with {len(series)} series\n")
        f.write('\n')
        for n in sorted(nr_series.keys()):
            f.write(f"    {nr_series[n]} with {n} series\n")







if __name__=='__main__':

    BUILD = r'C:\Users\md1spsx\Documents\Data\iBEAt_Build'
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", type=str, default=BUILD, help="Build folder")
    args = parser.parse_args()

    build = os.path.join(args.build, 't2star')
    os.makedirs(build, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(build, 'stage_3_check.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    run(args.build)