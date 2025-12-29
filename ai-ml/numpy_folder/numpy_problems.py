import numpy as np

# 🟢 LEVEL 1: Data Creation & Inspection

# 1️⃣ Dataset generation

# Create a dataset X with:

# 200 samples

# 4 features

# Values drawn from a normal distribution (mean = 5, std = 1.5)

# Print:

# shape

# mean of each feature

# standard deviation of each feature

rng = np.random.default_rng(42)

dataset = rng.normal(5,1.5,(200,4))

mean = dataset.mean(axis=0)
std = dataset.std(axis=0)

print (dataset.shape)
print(mean)
print(std)

# 2️⃣ Data type control

# Convert X to float32 and verify the data type.
dataset = dataset.astype(np.float32)

print(dataset.dtype)

# 3️⃣ Basic slicing

# Extract:

# first 10 samples

# last 2 features of all samples

print(dataset[:10,2:])

# 🟡 LEVEL 2: Statistics & Preprocessing
# 4️⃣ Feature-wise normalization

# Standardize X so that:

# each feature has mean = 0

# std = 1

# Verify by printing the new mean and std.

dataset= (dataset-mean)/std

print(dataset.mean(axis=0),dataset.std(axis=0))

# 5️⃣ Min–Max scaling

# Scale all features of X to the range [0, 1].

min_value = dataset.min(axis=0)
max_value = dataset.max(axis=0)

dataset = (dataset-min_value)/(max_value-min_value)

print(dataset.min(axis=0),dataset.max(axis=0))

# 6️⃣ Missing value simulation

# Randomly set 5% of the values in X to NaN.

mask = rng.random(dataset.shape) < 0.05 # (rng.random(dataset.shape)) this creates a an array with same dimention as dataset with values [0,1) (< 0.05) this condition changes 5% of the array to true and rest to false.
dataset[mask] = np.nan # which is then used here to determine which values to turn to NaN in the array dataset.

print(dataset)

# 7️⃣ Handle missing values

# Replace NaN values with the mean of the corresponding feature.

mask = np.isnan(dataset) # since nan is not a value we cant even caompare it to itself(== np.nan) so have to use np.isnan() func. 

col_mean = np.nanmean(dataset,axis=0) # np.nanmean() calc mean while ignoring nan values.

dataset[mask] = np.take(col_mean,np.where(mask)[1]) # here np.take(array,inecies) takes the correct mean from the col_mean array by getting the correct indicies by np.where() func and the [1] returns only the column indecies in this [j] format instead of [i,j] this.

print(dataset)

# 🟠 LEVEL 3: Masking, Broadcasting & Noise
# 8️⃣ Boolean masking

# Select all values in X that are: greater than (mean + 2 * std)

mean = dataset.mean(axis=0)
std = dataset.std(axis=0)
condition = mean + 2 * std
mask = dataset > condition

selected_ele = dataset[mask]
print(selected_ele)

# 9️⃣ Add Gaussian noise

# Add Gaussian noise (mean = 0, std = 0.2) to X using broadcasting.

# DEFINATION:-
# Gaussian noise means: Add small random values to your data, where the randomness follows a normal (bell-shaped) distribution(Gaussian noise is random noise drawn from a normal distribution with zero mean and small standard deviation. It is added to numerical data to simulate real-world variability. Broadcasting allows feature-wise noise to be added efficiently without explicit loops.).

nums = rng.integers(1,10,size=(4,3))
print(nums)

noise = rng.normal(loc=0,scale=0.2,size=nums.shape)
nums = nums + noise

print(nums)

# 🔟 Feature-wise centering

# Subtract the mean of each feature from X using broadcasting (no loops).

mean = np.mean(nums,axis=0)
nums = nums - mean

print(nums)

# 🔵 LEVEL 4: ML-style Data Splits & Labels
# 1️⃣1️⃣ Create labels

# Create a label vector y such that:

# y = 1 if the sum of features of a sample > threshold

# y = 0 otherwise
# (Choose a reasonable threshold.)

mask = nums.sum(axis=1) > 2
y = np.zeros(nums.shape[0],dtype=int)
y[mask] = 1 
y[~ mask] = 0

print(y)

# 1️⃣2️⃣ Shuffle data

# Shuffle X and y together while maintaining correspondence.

perm = rng.permutation(nums.shape[0])

shuffeled_nums = nums[perm]
shuffeled_y = y[perm]

print(shuffeled_nums,shuffeled_y)

# 1️⃣3️⃣ Train-test split

# Split the dataset into:

# 75% training

# 25% testing
# Using only NumPy.

random_vals = rng.random(dataset.shape[0])

mask = random_vals <= 0.25

testing = dataset[mask]
training = dataset[~mask]

print(testing.shape,training.shape)