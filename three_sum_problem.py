# Function to find all unique triplets in the array which gives the sum of zero
def find_triplets(arr):
    # Sort the array
    arr.sort()
    
    # List to store the result
    triplets = []
    
    # Looping through the array
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue  # Avoiding duplicate triplets
        
        left = i + 1  # Left pointer
        right = len(arr) - 1  # Right pointer
        
        # Finding triplets
        while left < right:
            total_sum = arr[i] + arr[left] + arr[right]
            if total_sum == 0:
                # Triplet found
                triplets.append([arr[i], arr[left], arr[right]])
                
                # Avoid duplicates in triplets
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif total_sum < 0:
                left += 1
            else:
                right -= 1
                
    return triplets

# Main function
if __name__ == "__main__":
    # Example array
    arr = [-1, 0, 1, 2, -1, -4]
    
    # Calling the function to find triplets
    result = find_triplets(arr)
    
    # Printing the result
    print("Unique triplets with sum zero:")
    for triplet in result:
        print(triplet)
