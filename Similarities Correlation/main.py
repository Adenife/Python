import module1
import module2

# NB: All try and except codes are used to catch errors that could occur during the running of the program so it does'nt affect the program flow 

print("User interface (main module)")

# define instructions to be printed on screen
alert_message = "Enter "
dict_message = "Enter 1 to check similatites between Artist \nEnter 2 to check similarities between Music tracks.\nEnter any other number to quit.\n"
metric_message = "Enter 1 to use Euclidean Similarity \nEnter 2 to use Cosine Similarity \nEnter 3 to use Pearson Correlation \nEnter 4 to use Jaccard Similarity \nEnter 5 to use Manhattan Similarity\n"
id1_message = "Enter first id to compare.\n"
id2_message = "Enter second id to compare.\n"


# while the program is running, until user terminates program
while True:
    
    try:
    
        # take in the dictionary object to be used
        dict_to_use = int(input(f'{dict_message}> '))


        # conditional statements to get desired result
        if dict_to_use == 1:
            #     call in the desired dictionary stated
            data = module1.artist

            
            try:
                #     take in desired metric to be used
                metric_to_use = int(input(f'{metric_message}> '))

                if metric_to_use == 1:
                    try:
                        #         Take in the ids of music to be compared
                        first_id = int(input(f'{id1_message}> '))
                        second_id = int(input(f'{id2_message}> '))

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.euclidean_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                        
                    except ValueError:
                        print("Enter a Number!!!")
                        continue

                elif metric_to_use == 2:
                    try:
                        #         Take in the ids of music to be compared
                        first_id = int(input(f'{id1_message}> '))
                        second_id = int(input(f'{id2_message}> '))

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.cosine_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                            
                    except ValueError:
                        print("Enter a Number!!!")
                        continue

                elif metric_to_use == 3:
                    try:
                        #         Take in the ids of music to be compared
                        first_id = int(input(f'{id1_message}> '))
                        second_id = int(input(f'{id2_message}> '))

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.pearson_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                        
                    except ValueError:
                        print("Enter a Number!!!")
                        continue

                elif metric_to_use == 4:
                    try:
                        #         Take in the ids of music to be compared
                        first_id = int(input(f'{id1_message}> '))
                        second_id = int(input(f'{id2_message}> '))

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.jaccard_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                            
                    except ValueError:
                        print("Enter a Number!!!")
                        continue

                elif metric_to_use == 5:
                    try:
                        #         Take in the ids of music to be compared
                        first_id = int(input(f'{id1_message}> '))
                        second_id = int(input(f'{id2_message}> '))

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.manhattan_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                        
                    except ValueError:
                        print("Enter a Number!!!")
                        continue
        
                else:
                    print('Enter a valid number!!!')
                    
            except ValueError:
                print("Enter a Number!!!")
                continue


        elif dict_to_use == 2:
            #     call in the desired dictionary stated
            data = module1.music
            
            try:
                #     take in desired metric to be used
                metric_to_use = int(input(f'{metric_message}> '))

                if metric_to_use == 1:
                    try:
                        #         Take in the ids of artist to be compared
                        first_id = input(f'{id1_message}> ')
                        second_id = input(f'{id2_message}> ')

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.euclidean_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                            
                    except ValueError:
                        print("Invalid key press!!!")
                        continue

                elif metric_to_use == 2:
                    try:
                        #         Take in the ids of artist to be compared
                        first_id = input(f'{id1_message}> ')
                        second_id = input(f'{id2_message}> ')

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.cosine_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                        
                    except ValueError:
                        print("Enter a Number!!!")
                        continue

                elif metric_to_use == 3:
                    try:
                        #         Take in the ids of artist to be compared
                        first_id = input(f'{id1_message}> ')
                        second_id = input(f'{id2_message}> ')

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.pearson_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                            
                    except ValueError:
                        print("Enter a Number!!!")
                        continue

                elif metric_to_use == 4:
                    try:
                        #         Take in the ids of artist to be compared
                        first_id = input(f'{id1_message}> ')
                        second_id = input(f'{id2_message}> ')

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.jaccard_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                        
                    except ValueError:
                        print("Enter a Number!!!")
                        continue


                elif metric_to_use == 5:
                    try:
                        #         Take in the ids of artist to be compared
                        first_id = input(f'{id1_message}> ')
                        second_id = input(f'{id2_message}> ')

                        if first_id in data.keys() and second_id in data.keys():
                            #         call in the required function to be used
                            print(f'The similarity value is: {module2.manhattan_similarity(data, first_id, second_id)}')
                        else:
                            print('Key does not exist!!!')
                        
                    except ValueError:
                        print("Enter a Number!!!")
                        continue
                    
                else:
                    print('Enter a valid number!!!')
            
            except ValueError:
                print("Enter a Number!!!")
                continue
                
        else:
            print('Thank you for using this service. Bye')
            break
                
                
                
    except ValueError:
        print("Enter a Number!!!")
        continue