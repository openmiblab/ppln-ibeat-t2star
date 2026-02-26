import os
import logging
import argparse
from pathlib import Path
import tempfile
import zipfile
import logging

import dbdicom as db

import utils.ibeat as ibeat




def list_zip_files(root_folder):
    return [str(p) for p in Path(root_folder).rglob("*.zip")]

def extract_to_db(dir, db_clean, site=None):
    try:
        existing_series = db.series(db_clean)
        for zip_file in list_zip_files(dir):
            try:
                with tempfile.TemporaryDirectory() as temp_dir:
                    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                        zip_ref.extractall(temp_dir)
                    for series_xnat in db.series(temp_dir):
                        for image_type, split_series_xnat in db.split_series(series_xnat, 'ImageType'):
                            series_clean = harmonize_series(zip_file, split_series_xnat, image_type, db_clean, site)
                            if series_clean is None:
                                continue
                            if series_clean not in existing_series:
                                db.copy(split_series_xnat, series_clean)
                                logging.info(f"Created series {series_clean[1:]} --- from file {zip_file}")

            except zipfile.BadZipFile:
                logging.error(f"Invalid zip file: {zip_file}. ")
            except:
                logging.exception(f"Unknown exception while cleaning {zip_file}. ")
    except:
        logging.exception(f"Unknown exception while extracting {dir}. ")



def harmonize_series(zip_file, series_xnat, image_type, db_dest, site=None):

    pt_id_clean = ibeat.clean_patient_id(series_xnat, site)
    if pt_id_clean is None:
        return
    st_desc_clean = ibeat.clean_study_desc(zip_file, series_xnat, site)
    if st_desc_clean is None:
        return
    sr_desc_clean = ibeat.clean_series_desc_t2star(series_xnat, image_type)
    if sr_desc_clean is None:
        return

    return [db_dest, pt_id_clean, (st_desc_clean, 0), (sr_desc_clean, 0)]




def run(build):

    # Download folder
    dir_download = os.path.join(build, 't2star', 'stage_1_download')

    # Define new DICOM databases
    db_patients = os.path.join(build, 't2star', 'stage_2_database', 'Patients')
    db_controls = os.path.join(build, 't2star', 'stage_2_database', 'Controls')
    # db_bari = os.path.join(dir_patients, 'Bari')
    # db_bordeaux = os.path.join(dir_patients, 'Bordeaux')
    # db_exeter = os.path.join(dir_patients, 'Exeter')
    # db_leeds = os.path.join(dir_patients, 'Leeds')
    # db_sheffield = os.path.join(dir_patients, 'Sheffield')
    # db_turku = os.path.join(dir_patients, 'Turku')

    # Folders with control data
    ctrls = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Bari', 'Bari_Volunteers_Repeatability'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Bordeaux', 'Bordeaux_Volunteers_Repeatability_Baseline'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Exeter', 'Exeter_setup_scans'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Exeter', 'Exeter_Volunteer'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Leeds', 'Leeds_setup_scans'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Leeds', 'Leeds_volunteer_repeatability_study'),
        os.path.join(dir_download, 'ibeat_setup'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Turku', 'Turku_volunteer_repeatability_study'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Turku', 'Turku_Volunteers_GE_Repeatability'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Turku', 'Turku_GE_Setup_Tests'),
    ]
    
    # Folders with patient data
    pts_bari = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Bari', 'Bari_Patients'),
    ]
    pts_bordeaux = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Bordeaux', 'Bordeaux_Patients_Baseline'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Bordeaux', 'Bordeaux_Patients_Followup'),
    ]
    pts_exeter = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Exeter', 'Exeter_Patients_Baseline'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Exeter', 'Exeter_Patients_Followup'),
    ]
    pts_leeds = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Leeds', 'Leeds_Patients'),
    ]
    pts_sheffield = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Sheffield'),
    ]
    pts_turku = [
        os.path.join(dir_download, 'BEAt-DKD-WP4-Turku', 'Turku_Patients_Philips'),
        os.path.join(dir_download, 'BEAt-DKD-WP4-Turku', 'Turku_Patients_GE'),
    ]

    # Build DICOM databases
    [extract_to_db(dir, db_controls) for dir in ctrls]
    [extract_to_db(dir, db_patients, 'Bari') for dir in pts_bari]
    [extract_to_db(dir, db_patients, 'Bordeaux') for dir in pts_bordeaux]
    [extract_to_db(dir, db_patients, 'Exeter') for dir in pts_exeter]
    [extract_to_db(dir, db_patients, 'Leeds') for dir in pts_leeds]
    [extract_to_db(dir, db_patients, 'Sheffield') for dir in pts_sheffield]
    [extract_to_db(dir, db_patients, 'Turku') for dir in pts_turku]
    


if __name__=='__main__':

    BUILD = r'C:\Users\md1spsx\Documents\Data\iBEAt_Build'
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", type=str, default=BUILD, help="Build folder")
    args = parser.parse_args()

    path = os.path.join(args.build, 't2star')
    os.makedirs(path, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(path, 'stage_2_database.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.getLogger("pydicom").setLevel(logging.ERROR)
   
    run(args.build)
