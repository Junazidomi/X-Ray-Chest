import os
from tensorflow.keras.callbacks import Callback

class CustomCallback(Callback):
    def on_epoch_end(self, epoch, logs=None):
        logs=logs or {}

        val_acc=logs.get('val_accuracy')
        val_loss=logs.get('val_loss')

        if val_acc is not None and val_loss is not None:
            if val_acc >=0.9 and val_loss<=0.4:
                print(f"\nTraining model stopped: val_accuracy {val_acc:.2f}, val_loss{val_loss:.2f}")
                self.model.stop_training=True


def train_model(model, train_generator, validation_generator):
    history=model.fit(
        train_generator,
        epochs=50,
        batch_size=32,
        validation_data=validation_generator,
        callbacks=[CustomCallback()]
    )

    return history