import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



# Defining global variables
# Number of samples
N = 0


def compute_l1_sensitivity(original_data, actual_average_age):

	max_difference = 0
	for i in range(len(original_data)):
		new_data, list_a, list_b = [], [], []
		list_a = list(original_data[:i])
		list_b = list(original_data[i+1:])
		for ele in list_a:
			new_data.append(ele)
		for ele in list_b:
			new_data.append(ele)
		print(i, len(original_data),len(new_data))
		current_difference = abs(actual_average_age - get_average_age(new_data))
		if current_difference > max_difference:
			max_difference = current_difference
	l1_sensitivity = max_difference

	return l1_sensitivity



def compute_l2_sensitivity(original_data, actual_average_age):

	max_difference = 0
	for i in range(len(original_data)):
		new_data, list_a, list_b = [], [], []
		list_a = list(original_data[:i])
		list_b = list(original_data[i+1:])
		for ele in list_a:
			new_data.append(ele)
		for ele in list_b:
			new_data.append(ele)
		print(i, len(original_data),len(new_data))
		current_difference = abs(actual_average_age - get_average_age(new_data))
		if current_difference > max_difference:
			max_difference = current_difference
	l2_sensitivity = max_difference

	return l2_sensitivity
	


def laplacian_mechanism_on_age(data):

	global N;

	original_data = data[:]["age"].tolist()
	actual_average_age = get_average_age(original_data)
	# compute_l1_sensitivity(original_data, actual_average_age)
	l1_sensitivity = 0.0010520497409984841
	print(l1_sensitivity)

	average_differences = []
	max_age = max(original_data) - 75
	epsilon_values = list(np.arange(0.05, max_age, 0.05))
	for epsilon in epsilon_values:
		scale_factor = l1_sensitivity/epsilon
		laplace_noise = np.random.laplace(scale=scale_factor, size=N)
		privatised_age = get_average_age(original_data + laplace_noise)
		average_differences.append(abs(actual_average_age - privatised_age))

	plt.plot(epsilon_values, average_differences)
	plt.show()

	return



def gaussian_mechanism_on_age(data):

	global N;

	original_data = data[:]["age"].tolist()
	actual_average_age = get_average_age(original_data)
	compute_l2_sensitivity(original_data, actual_average_age)
	# l2_sensitivity = 0.0010520497409984841
	print(l2_sensitivity)

	delta = 10e-5
	average_differences = []
	max_age = max(original_data) - 75
	epsilon_values = list(np.arange(0.05, max_age, 0.05))
	for epsilon in epsilon_values:
		scale_factor = l2_sensitivity/epsilon
		sigma = np.sqrt(2 * np.log(1.25 / delta)) * scale_factor
		gaussian_noise = np.random.normal(scale=sigma)
		privatised_age = get_average_age(original_data + gaussian_noise)
		average_differences.append(abs(actual_average_age - privatised_age))

	plt.plot(epsilon_values, average_differences)
	plt.show()

	return



def get_average_age(data):

	return np.average(data)



def main():

	global N;

	df = pd.read_csv("adult.csv")
	N = len(df)

	# laplacian_mechanism_on_age(df)
	gaussian_mechanism_on_age(df)

	return




if __name__ == "__main__":

	main()
