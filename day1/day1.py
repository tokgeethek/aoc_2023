with open('day1_input.txt') as input:
    input_array = [row.replace('\n','') for row in input]
    numbers = '0123456789'

    #Q1
    # find first number and last number
    first = ''
    last = ''
    calibration_value = 0
    q2_calibration_value = 0

    for row in input_array:
        for x in row:
            if x in numbers:
                last = x #loop to last num

        for y in row[::-1]:
            if y in numbers:
                first = y #loop to last num, in reverse

        calibration_value += int(first+last)

    #Q2
        q2_row = row
        q2_row_find_first = q2_row
        q2_row_find_last = q2_row

        q2_row_find_first = q2_row_find_first.replace('oneight','1').replace('threeight','3').replace('eightwo','8').replace('fiveight','5').replace('nineight','9').replace('twone','2').replace('sevenine','7').replace('eighthree','8').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')
        q2_row_find_last = q2_row_find_last.replace('oneight','8').replace('threeight','8').replace('eightwo','2').replace('fiveight','8').replace('nineight','8').replace('twone','1').replace('sevenine','9').replace('eighthree','3').replace('one','1').replace('two','2').replace('three','3').replace('four','4').replace('five','5').replace('six','6').replace('seven','7').replace('eight','8').replace('nine','9')

        for x in q2_row_find_last:
            if x in numbers:
                q2_last = x #loop to last num

        for y in q2_row_find_first[::-1]:
            if y in numbers:
                q2_first = y #loop to last num, in reverse
            
        q2_calibration_value += int(q2_first+q2_last)
        q2_first, q2_last = 0, 0
    
    print(calibration_value)
    print(q2_calibration_value)