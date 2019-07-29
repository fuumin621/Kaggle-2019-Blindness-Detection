from collections import OrderedDict

import torchvision
from catalyst.dl import ConfigExperiment

from retinopathy.augmentations import get_train_aug, get_test_aug
from retinopathy.dataset import get_datasets


class Experiment(ConfigExperiment):
    @staticmethod
    def get_transforms(stage: str = None, image_size=(512, 512), augmentation='medium', mode: str = None):
        if mode == 'train':
            return get_train_aug(image_size=image_size, augmentation=augmentation, crop_black=False)

        return get_test_aug(image_size=image_size, crop_black=False)

    def get_datasets(self, stage: str, **kwargs):
        datasets = OrderedDict()

        train_ds, valid_ds = get_datasets()

        datasets["train"] = train_ds
        datasets["valid"] = valid_ds

        return datasets
