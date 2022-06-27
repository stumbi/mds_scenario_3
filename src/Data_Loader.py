import os
import pandas as pd
from torch.utils.data import Dataset
from torchvision.io import read_image


class CustomImageDataset():
    def __init__(self, label_df):
        self.start_times = label_df['Start']
        self.sleep_labels = label_df['Schlafstadium']
        self.start_time = self.create_time(self.start_times)
        self.end_time = self.create_time(label_df[['Start']])
        self.start_id = self.get_id()

    def __len__(self):
        return len(self.sleep_labels)

    """
    def __getitem__(self, idx):
       img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        
        return 12
    """

    @staticmethod
    def create_time(frame_time):
        return frame_time.apply(change_time)

    # condition: patient has to wake up before 10am and go to sleep after 10am
    @staticmethod
    def change_time(time_string):
        time_string.replace(':', '')
        time_int = int(time_string)
        if len(time_int) <= 5:
            time_int += 240000
        return time_int

    def get_id(self):
        # find nearest start time
        st = self.create_time(self.start_times)
        self.iterate(st)

        correct_id = st.iloc[(st['Start'] - input).abs().argsort()[:2]].index
        return correct_id

    """
start time -> lese df -> wandle time in ints -> gehe durch df und suche korrekten idx -> gebe diese zeit an
    """


def main():
    path = '../data/Exercises_SS22/sleeplab_dataset_10hz/patient_29_male_7_years/sleep_staging.csv'
    label_df = pd.read_csv(path)

    cid = CustomImageDataset(label_df)


if __name__ == '__main__':
    main()
