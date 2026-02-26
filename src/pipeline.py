import os
import logging
import argparse

import stage_1_download
import stage_2_database
import stage_3_check


if __name__=='__main__':

    BUILD = r'C:\Users\md1spsx\Documents\Data\iBEAt_Build'
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--build", type=str, default=BUILD, help="Build folder")
    args = parser.parse_args()

    path = os.path.join(args.build, 't2star')
    os.makedirs(path, exist_ok=True)

    logging.basicConfig(
        filename=os.path.join(path, 'pipeline.log'),
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.getLogger("pydicom").setLevel(logging.ERROR)
  
    stage_1_download.run(args.build)
    stage_2_database.run(args.build)
    stage_3_check.run(args.build)