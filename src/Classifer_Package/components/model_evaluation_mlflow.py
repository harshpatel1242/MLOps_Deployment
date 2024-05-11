import tensorflow as tf
import logging
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from Classifer_Package.entity.config_entity import EvaluationConfig
from Classifer_Package.utils.common import read_yaml, create_directories,save_json


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.30
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        try:
            mlflow.set_registry_uri(self.config.mlflow_uri)
            tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

            # Log step 1: Set registry URI
            logging.info("Step 1: Setting MLflow registry URI")
            mlflow.log_param("Step 1", "Setting MLflow registry URI")

            with mlflow.start_run():
                # Log step 2: Starting MLflow run
                logging.info("Step 2: Starting MLflow run")
                mlflow.log_param("Step 2", "Starting MLflow run")

                mlflow.log_params(self.config.all_params)
                # Log step 3: Logging parameters
                logging.info("Step 3: Logging parameters")
                mlflow.log_param("Step 3", "Logging parameters")

                mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
                # Log step 4: Logging metrics
                logging.info("Step 4: Logging metrics")
                mlflow.log_param("Step 4", "Logging metrics")

                # Model registry does not work with file store
                if tracking_url_type_store != "file":
                    mlflow.keras.log_model(self.model, "model", registered_model_name="VGG16Model")
                    # Log step 5: Logging model (registry enabled)
                    logging.info("Step 5: Logging model (registry enabled)")
                    mlflow.log_param("Step 5", "Logging model (registry enabled)")
                else:
                    mlflow.keras.log_model(self.model, "model")
                    # Log step 6: Logging model (registry disabled)
                    logging.info("Step 6: Logging model (registry disabled)")
                    mlflow.log_param("Step 6", "Logging model (registry disabled)")

        except Exception as e:
            # Log the error message if an exception occurs
            logging.error(f"Error logging into MLflow: {e}")
            mlflow.log_param("Error", f"Error logging into MLflow: {e}")