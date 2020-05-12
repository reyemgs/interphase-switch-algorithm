import numpy as np  
           #Vx     V            noV        Izm       Rd        osc_sum
def sumthd(vec_x, v_struct, numof_value, wf_vector, dec_vector, wf_sum):

    sumof_values = [0, 0, 0]     #S
    wf_sum = np.zeros((3,104))  #Osc_sum
    numof_switching = 0         #perecl
    counter = 1                 #G

    for i in range(1, numof_value, 2):
        a = i - 1
        if vec_x[a] == 1:
            if vec_x[i] == 0:
                dec_vector[counter] = 3
                wf_sum[3:] = wf_sum[3:] + wf_vector[v_struct[2,counter]:]

        else:
            if vec_x[i] == 1:
                dec_vector[counter] = 2
                wf_sum[2:] = wf_sum[2:] + wf_vector[v_struct[2,counter]:]
        
            else:
                dec_vector[counter] = 1
                wf_sum[1:] = wf_sum[1:] + wf_vector[v_struct[2,counter]:]

        if dec_vector[counter] != v_struct[3,counter]:
            numof_switching += 1

        counter += 1
    #Hi
    #Вызов THD