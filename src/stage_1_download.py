"""
Automatic download of T2* data from XNAT.
"""

import os
import logging
import argparse

from miblab_data.xnat import download_series



def leeds_patients(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Leeds",
            subject_label="Leeds_Patients", #24 pancreas matrix 256 frames 144, 37 kidney matrix 512 frames 60
            attr = {
                "parameters/sequence": ["*fl2d12"],
                "parameters/fov/y": [512],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Leeds patients.")


def leeds_volunteers(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Leeds",
            subject_label="Leeds_volunteer_repeatability_study",
            attr = {
                "parameters/sequence": ["*fl2d12"],
                "parameters/fov/y": [512],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Leeds volunteers.")

def leeds_setup(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Leeds",
            subject_label="Leeds_setup_scans",
            attr = {
                "parameters/sequence": ["*fl2d12"],
                "parameters/fov/y": [512],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Leeds setup scans.")

def bari_patients(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Bari",
            subject_label="Bari_Patients",
            attr={
                "series_description": ["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Bari patients.")

def bari_volunteers(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Bari",
            subject_label="Bari_Volunteers_Repeatability",
            attr={
                "series_description": ["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Bari volunteers.")

def sheffield_patients(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Sheffield",
            #subject_label='IBE7128103', #tmp
            attr={
                "series_description":['T2star_map_kidneys_cor-oblique_mbh'],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Sheffield patients.")

def turku_ge_patients(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Turku",
            subject_label="Turku_Patients_GE",
            attr={
                "series_description": ["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Turku GE patients.")

def turku_ge_repeatability(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Turku",
            subject_label="Turku_Volunteers_GE_Repeatability",
            attr={
                "series_description": ["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Turku GE volunteers.")

def turku_ge_setup(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Turku",
            subject_label="Turku_GE_Setup_Tests",
            attr={
                "series_description": ["T2star_map_kidney_cor_mph"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Turku GE setup scans.")

def turku_philips_patients(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Turku",
            subject_label="Turku_Patients_Philips",
            attr={
                "series_description":["T2-star-map-kidneys-coronal-oblique-BH"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Turku Philips patients.")

def turku_philips_repeatability(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Turku",
            subject_label="Turku_volunteer_repeatability_study",
            attr={
                "series_description": ["T2-star-map-kidneys-coronal-oblique-BH"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Turku Philips volunteers.")

def bordeaux_patients_baseline(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Bordeaux",
            subject_label="Bordeaux_Patients_Baseline",
            # experiment_label='iBE-6128-005_baseline', # tmp
            attr={
                "series_description": [
                    "T2star_map_kidneys_cor-oblique_mbh", 
                    "T2Star_Images",
                ],
                "parameters/fov/y": [512], # This excludes T2Star_Images for pancreas
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Bordeaux patients.")

def bordeaux_volunteers(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Bordeaux",
            subject_label="Bordeaux_Volunteers_Repeatability_Baseline",
            attr={
                "series_description": [
                    "T2star_map_kidneys_cor-oblique_mbh", 
                    "T2Star_Images",
                ],
                "parameters/fov/y": [512], # This excludes T2Star_Images for pancreas
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Bordeaux volunteers.")

def bordeaux_patients_followup(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Bordeaux",
            subject_label="Bordeaux_Patients_Followup",
            attr={
                "series_description": [
                    "T2star_map_kidneys_cor-oblique_mbh", 
                    "T2Star_Images",
                ],
                "parameters/fov/y": [512], # This excludes T2Star_Images for pancreas
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Bordeaux patients.")

def exeter_patients_baseline(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Exeter",
            subject_label="Exeter_Patients_Baseline",
            attr={
                "series_description":["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Exeter patients baseline.")

def exeter_patients_followup(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Exeter",
            subject_label="Exeter_Patients_Followup",
            attr={
                "series_description":["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Exeter patients followup.")

def exeter_volunteers(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Exeter",
            subject_label="Exeter_Volunteer",
            attr={
                "series_description":["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Exter volunteers.")

def exeter_setup(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="BEAt-DKD-WP4-Exeter",
            subject_label="Exeter_setup_scans",
            attr={
                "series_description":["T2star_map_kidneys_cor-oblique_mbh"],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Exeter setup.")


def sheffield_setup(path, n_max=None):
    try:
        download_series(
            xnat_url="https://qib.shef.ac.uk",
            output_dir=path,
            project_id="ibeat_setup",
            attr={
                "series_description":['T2star_map_kidneys_cor-oblique_mbh'],
            },
            log=True,
            n_max=n_max,
        )
    except:
        logging.exception(f"Error downloading Sheffield setup scans.")


def run(build):

    path = os.path.join(build, 't2star', 'stage_1_download')
    n_max=None

    leeds_patients(path, n_max)
    bari_patients(path, n_max)
    sheffield_patients(path, n_max)
    turku_ge_patients(path, n_max)
    turku_philips_patients(path, n_max)
    bordeaux_patients_baseline(path, n_max)
    bordeaux_patients_followup(path, n_max)
    exeter_patients_baseline(path, n_max)
    exeter_patients_followup(path, n_max)

    bari_volunteers(path, n_max)
    leeds_volunteers(path, n_max)
    bordeaux_volunteers(path, n_max)
    exeter_volunteers(path, n_max)
    turku_philips_repeatability(path, n_max)
    turku_ge_repeatability(path, n_max)
    
    leeds_setup(path, n_max)
    exeter_setup(path, n_max)
    turku_ge_setup(path, n_max)
    sheffield_setup(path, n_max)


if __name__=='__main__':

    BUILD = r'C:\Users\md1spsx\Documents\Data\iBEAt_Build'
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", type=str, default=BUILD, help="Build folder")
    args = parser.parse_args()

    path = os.path.join(args.build, 't2star')
    os.makedirs(path, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(path, 'stage_1_download.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
   
    run(args.build)


