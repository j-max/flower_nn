import os, shutil


new_dir = 'split/'
# path to original directory for each flower
data_rose_dir = 'flowers/rose/'
data_daisy_dir = 'flowers/daisy/'
data_dandelion_dir = 'flowers/dandelion/'
data_sunflower_dir = 'flowers/sunflower/'
data_tulip_dir = 'flowers/tulip/'

# Create list of all the image filepaths for each flower
# running the print statements below shows sunflowers to have the least images at 734

imgs_rose = [file for file in os.listdir(data_rose_dir) if file.endswith('.jpg')]
print('There are', len(imgs_rose), 'rose images')

imgs_tulip = [file for file in os.listdir(data_tulip_dir) if file.endswith('.jpg')]
print('There are', len(imgs_tulip), 'tulip images')

imgs_daisy = [file for file in os.listdir(data_daisy_dir) if file.endswith('.jpg')]
print('There are', len(imgs_daisy), 'daisy images')

imgs_dandelion = [file for file in os.listdir(data_dandelion_dir) if file.endswith('.jpg')]
print('There are', len(imgs_dandelion), 'dandelion images')

imgs_sunflower = [file for file in os.listdir(data_sunflower_dir) if file.endswith('.jpg')]
print('There are', len(imgs_sunflower), 'sunflower images')


# Create strings of paths to each train/val/test folder which will be created below
train_folder = os.path.join(new_dir, 'train')
test_folder = os.path.join(new_dir, 'test')
val_folder = os.path.join(new_dir, 'val')

train_rose = os.path.join(train_folder, 'rose')
test_rose = os.path.join(test_folder, 'rose')
val_rose = os.path.join(val_folder, 'rose')

train_tulip = os.path.join(train_folder, 'tulip')
test_tulip = os.path.join(test_folder, 'tulip')
val_tulip = os.path.join(val_folder, 'tulip')

train_daisy = os.path.join(train_folder, 'daisy')
test_daisy = os.path.join(test_folder, 'daisy')
val_daisy = os.path.join(val_folder, 'daisy')

train_dandelion = os.path.join(train_folder, 'dandelion')
test_dandelion = os.path.join(test_folder, 'dandelion')
val_dandelion = os.path.join(val_folder, 'dandelion')

train_sunflower = os.path.join(train_folder, 'sunflower')
test_sunflower = os.path.join(test_folder, 'sunflower')
val_sunflower = os.path.join(val_folder, 'sunflower')

# Make each directory
os.mkdir(new_dir)

os.mkdir(train_folder)
os.mkdir(val_folder)
os.mkdir(test_folder)

os.mkdir(train_rose)
os.mkdir(val_rose)
os.mkdir(test_rose)

os.mkdir(train_tulip)
os.mkdir(val_tulip)
os.mkdir(test_tulip)

os.mkdir(train_daisy)
os.mkdir(val_daisy)
os.mkdir(test_daisy)

os.mkdir(train_dandelion)
os.mkdir(val_dandelion)
os.mkdir(test_dandelion)

os.mkdir(train_sunflower)
os.mkdir(val_sunflower)
os.mkdir(test_sunflower)

# splits for each flower
imgs = imgs_tulip[:500]
for img in imgs:
    origin = os.path.join(data_tulip_dir, img)
    destination = os.path.join(train_tulip, img)
    shutil.copyfile(origin, destination)

imgs = imgs_tulip[500:624]
for img in imgs:
    origin = os.path.join(data_tulip_dir, img)
    destination = os.path.join(val_tulip, img)
    shutil.copyfile(origin, destination)

imgs = imgs_tulip[624:624 + 156]
for img in imgs:
    origin = os.path.join(data_tulip_dir, img)
    destination = os.path.join(test_tulip, img)
    shutil.copyfile(origin, destination)

######### daisy ###########
imgs = imgs_daisy[:500]
for img in imgs:
    origin = os.path.join(data_daisy_dir, img)
    destination = os.path.join(train_daisy, img)
    shutil.copyfile(origin, destination)

imgs = imgs_daisy[500:624]
for img in imgs:
    origin = os.path.join(data_daisy_dir, img)
    destination = os.path.join(val_daisy, img)
    shutil.copyfile(origin, destination)

imgs = imgs_daisy[624:624 + 156]
for img in imgs:
    origin = os.path.join(data_daisy_dir, img)
    destination = os.path.join(test_daisy, img)
    shutil.copyfile(origin, destination)

########dandelion###########
imgs = imgs_dandelion[:500]
for img in imgs:
    origin = os.path.join(data_dandelion_dir, img)
    destination = os.path.join(train_dandelion, img)
    shutil.copyfile(origin, destination)

imgs = imgs_dandelion[500:624]
for img in imgs:
    origin = os.path.join(data_dandelion_dir, img)
    destination = os.path.join(val_dandelion, img)
    shutil.copyfile(origin, destination)

imgs = imgs_dandelion[624:624 + 156]
for img in imgs:
    origin = os.path.join(data_dandelion_dir, img)
    destination = os.path.join(test_dandelion, img)
    shutil.copyfile(origin, destination)

########rose###########
imgs = imgs_rose[:500]
for img in imgs:
    origin = os.path.join(data_rose_dir, img)
    destination = os.path.join(train_rose, img)
    shutil.copyfile(origin, destination)

imgs = imgs_rose[500:624]
for img in imgs:
    origin = os.path.join(data_rose_dir, img)
    destination = os.path.join(val_rose, img)
    shutil.copyfile(origin, destination)

imgs = imgs_rose[624:624 + 156]
for img in imgs:
    origin = os.path.join(data_rose_dir, img)
    destination = os.path.join(test_rose, img)
    shutil.copyfile(origin, destination)

########sunflower###########
imgs = imgs_sunflower[:500]
for img in imgs:
    origin = os.path.join(data_sunflower_dir, img)
    destination = os.path.join(train_sunflower, img)
    shutil.copyfile(origin, destination)

imgs = imgs_sunflower[500:624]
for img in imgs:
    origin = os.path.join(data_sunflower_dir, img)
    destination = os.path.join(val_sunflower, img)
    shutil.copyfile(origin, destination)

imgs = imgs_sunflower[624:624 + 156]
for img in imgs:
    origin = os.path.join(data_sunflower_dir, img)
    destination = os.path.join(test_sunflower, img)
    shutil.copyfile(origin, destination)

