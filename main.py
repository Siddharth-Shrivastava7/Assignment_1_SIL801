import torch
from torchvision import datasets
from torch.utils.data.sampler import SubsetRandomSampler


data_dir = '/data_folder'

def load_split_train_test(datadir, valid_size = .2):
    train_transforms = transforms.Compose([
                                        transforms.ToTensor(),
                                       ])
    test_transforms = transforms.Compose([
                                      transforms.ToTensor(),
                                      ])
    train_data = datasets.ImageFolder(datadir,       
                    transform=train_transforms)

    test_data = datasets.ImageFolder(datadir,
                    transform=test_transforms)

    num_train = len(train_data)
    indices = list(range(num_train))
    split = int(np.floor(valid_size * num_train))
    np.random.shuffle(indices)

    train_idx, test_idx = indices[split:], indices[:split]
    train_sampler = SubsetRandomSampler(train_idx)
    test_sampler = SubsetRandomSampler(test_idx)
    trainloader = torch.utils.data.DataLoader(train_data,
                   sampler=train_sampler, batch_size=64)
    testloader = torch.utils.data.DataLoader(test_data,
                   sampler=test_sampler, batch_size=64)
    return trainloader, testloader

    trainloader, testloader = load_split_train_test(data_dir, .2)
    
    # print(trainloader.dataset.classes)



