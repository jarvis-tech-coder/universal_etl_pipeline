import os
import shutil
import logging

from etl_scripts.extract import extract
from etl_scripts.transform import transform
from etl_scripts.load import load
from etl_scripts.generate_report import generate_report
from etl_scripts.logger import setup_logger
from config.config import DATA_INCOMING, DATA_PROCESSED, LOG_PATH


def run_pipeline():
    setup_logger()
    logging.info("ETL pipeline started")

    for filename in os.listdir(DATA_INCOMING):
        source_path = os.path.join(DATA_INCOMING, filename)

        if not os.path.isfile(source_path):
            continue

        try:
            logging.info(f"Processing file: {filename}")

            df = extract(source_path)
            df = transform(df)
            load(df)

            shutil.move(
                source_path,
                os.path.join(DATA_PROCESSED, filename)
            )

            logging.info(f"File processed successfully: {filename}")

        except Exception as e:
            logging.error(f"Failed processing {filename}: {e}")

        try:
            generate_report()
        except Exception as e:
            logging.warning(f"Report generation skipped: {e}")

    logging.info("ETL pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
