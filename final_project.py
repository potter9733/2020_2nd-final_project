import math
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

excel_file = 'mers_data.xlsx'

df = pd.read_excel(excel_file)

a, b, dt = 0, 49, 1
n = math.floor((b-a) / dt)

E = [21]
I = [7]
J = [2]
R = [0]
S = [10000 - E[0] - I[0] - J[0]]

t = [0]
N = 10000

day = [''] * 50
day[0] = '05-20'
day[10] = '05-30'
day[20] = '06-09'
day[30] = '06-19'
day[40] = '06-29'
day[49] = '07-08'

# SSE's Transmission rate
beta_star_1 = 85/4
beta_star_2 = 24/9

# Starting time (after the outbreak onset)
t_1 = 7
t_2 = 2

# Duration of exposure
delta_1 = 3
delta_2 = 8

# Contact reduction in isolated individuals after case confirmed
l = 0.1

# (1 / kappa) = Incubation period
kappa = 1 / 6.83

# Isolation rate
alpha_0 = 1 / 6
alpha_1 = 1 / 2

# (1 / gamma) = Period of hospital stay
gamma = 1 / 13

# Transmission rate
beta_0 = 0.06
beta_1 = 0.03

# def create_SSs():
#     import numpy as np
#     n = np.random.randint(1, 6)
#     arr = [[None]*3 for _ in range(n)]
    
#     for i in range(n):
#         arr[i][0], arr[i][1], arr[i][2] =  np.random.randint(2, 11), np.random.randint(3, 11), np.random.randint(20, 101)
        
#     return arr

for i in range(n):
    if i <= 18:
        beta = beta_0
        alpha = alpha_0
        l = 0.1
    else:
        beta = beta_1
        alpha = alpha_1
    # Heaviside step function
    if t_1 <= i <= t_1 + delta_1:
        Heaviside_function_1 = 1
    else:
        Heaviside_function_1 = 0
        
    if t_2 <= i <= t_2 + delta_2:
        Heaviside_function_2 = 1
    else:
        Heaviside_function_2 = 0
    
    S.append(S[i] + dt * (
                            (-beta) * (I[i] + l * J[i]) * S[i] / N 
                          + (-beta_star_1) * Heaviside_function_1
                          + (-beta_star_2) * Heaviside_function_2
                          )
            )
    
    E.append(E[i] + dt * (
                            (beta) * (I[i] + l * J[i]) * S[i] / N 
                          + (beta_star_1) * Heaviside_function_1
                          + (beta_star_2) * Heaviside_function_2
                          - kappa * E[i]
                          )
            )
    
    I.append(I[i] + dt * (kappa * E[i] - alpha * I[i]))
    
    # J.append(J[i] + dt * (alpha * I[i] - gamma * J[i]))
    J.append(J[i] + dt * (alpha * I[i]))
    # J.append(J[i] + dt * (kappa * E[i]))
    
    R.append(R[i] + dt * gamma * J[i])
    
    t.append(t[i] + dt)

plt.figure()
# plt.plot(t, S)
# plt.plot(t, E, 'b') # currently exposed MERS but no symptoms
# plt.plot(t, I, 'g') # symptoms; but not confirmed
plt.plot(t, J, 'r') # identified and confirmed; thus, isolated
# plt.plot(t, R, 'r') # cured or deceased
# plt.plot(t, df['일별'], 'o-')
#plt.plot(t, df['누적'], 'o-')
plt.xticks(np.arange(0, 50), labels = day)

a, b, dt = 0, 49, 1
n = math.floor((b-a) / dt)

E = [21]
I = [7]
J = [2]
R = [0]
S = [10000 - E[0] - I[0] - J[0]]

t = [0]
N = 10000

day = [''] * 50
day[0] = '05-20'
day[10] = '05-30'
day[20] = '06-09'
day[30] = '06-19'
day[40] = '06-29'
day[49] = '07-08'

# SSE's Transmission rate
beta_star_1 = 85/4
beta_star_2 = 24/9

# Starting time (after the outbreak onset)
t_1 = 7
t_2 = 2

# Duration of exposure
delta_1 = 3
delta_2 = 8

# Contact reduction in isolated individuals after case confirmed
l = 0.1

# (1 / kappa) = Incubation period
kappa = 1 / 6.83

# Isolation rate
alpha_0 = 1 / 6
alpha_1 = 1 / 2

# (1 / gamma) = Period of hospital stay
gamma = 1 / 13

# Transmission rate
beta_0 = 0.06
beta_1 = 0.03

# def create_SSs():
#     import numpy as np
#     n = np.random.randint(1, 6)
#     arr = [[None]*3 for _ in range(n)]
    
#     for i in range(n):
#         arr[i][0], arr[i][1], arr[i][2] =  np.random.randint(2, 11), np.random.randint(3, 11), np.random.randint(20, 101)
        
#     return arr

for i in range(n):
    if i <= 11:
        beta = beta_0
        alpha = alpha_0
        l = 0.1
    else:
        beta = beta_1
        alpha = alpha_1
    # Heaviside step function
    if t_1 <= i <= t_1 + delta_1:
        Heaviside_function_1 = 1
    else:
        Heaviside_function_1 = 0
        
    if t_2 <= i <= t_2 + delta_2:
        Heaviside_function_2 = 1
    else:
        Heaviside_function_2 = 0
    
    S.append(S[i] + dt * (
                            (-beta) * (I[i] + l * J[i]) * S[i] / N 
                          + (-beta_star_1) * Heaviside_function_1
                          + (-beta_star_2) * Heaviside_function_2
                          )
            )
    
    E.append(E[i] + dt * (
                            (beta) * (I[i] + l * J[i]) * S[i] / N 
                          + (beta_star_1) * Heaviside_function_1
                          + (beta_star_2) * Heaviside_function_2
                          - kappa * E[i]
                          )
            )
    
    I.append(I[i] + dt * (kappa * E[i] - alpha * I[i]))
    
    # J.append(J[i] + dt * (alpha * I[i] - gamma * J[i]))
    J.append(J[i] + dt * (alpha * I[i]))
    # J.append(J[i] + dt * (kappa * E[i]))
    
    R.append(R[i] + dt * gamma * J[i])
    
    t.append(t[i] + dt)


# plt.plot(t, S)
# plt.plot(t, E, 'b') # currently exposed MERS but no symptoms
# plt.plot(t, I, 'g') # symptoms; but not confirmed
plt.plot(t, J, 'b') # identified and confirmed; thus, isolated
# plt.plot(t, R, 'r') # cured or deceased
# plt.plot(t, df['일별'], 'o-')
#plt.plot(t, df['누적'], 'o-')
plt.xticks(np.arange(0, 50), labels = day)

a, b, dt = 0, 49, 1
n = math.floor((b-a) / dt)

E = [21]
I = [7]
J = [2]
R = [0]
S = [10000 - E[0] - I[0] - J[0]]

t = [0]
N = 10000

day = [''] * 50
day[0] = '05-20'
day[10] = '05-30'
day[20] = '06-09'
day[30] = '06-19'
day[40] = '06-29'
day[49] = '07-08'

# SSE's Transmission rate
beta_star_1 = 85/4
beta_star_2 = 24/9

# Starting time (after the outbreak onset)
t_1 = 7
t_2 = 2

# Duration of exposure
delta_1 = 3
delta_2 = 8

# Contact reduction in isolated individuals after case confirmed
l = 0.1

# (1 / kappa) = Incubation period
kappa = 1 / 6.83

# Isolation rate
alpha_0 = 1 / 6
alpha_1 = 1 / 2

# (1 / gamma) = Period of hospital stay
gamma = 1 / 13

# Transmission rate
beta_0 = 0.06
beta_1 = 0.03

# def create_SSs():
#     import numpy as np
#     n = np.random.randint(1, 6)
#     arr = [[None]*3 for _ in range(n)]
    
#     for i in range(n):
#         arr[i][0], arr[i][1], arr[i][2] =  np.random.randint(2, 11), np.random.randint(3, 11), np.random.randint(20, 101)
        
#     return arr

for i in range(n):
    if i <= 4:
        beta = beta_0
        alpha = alpha_0
        l = 0.1
    else:
        beta = beta_1
        alpha = alpha_1
    # Heaviside step function
    if t_1 <= i <= t_1 + delta_1:
        Heaviside_function_1 = 1
    else:
        Heaviside_function_1 = 0
        
    if t_2 <= i <= t_2 + delta_2:
        Heaviside_function_2 = 1
    else:
        Heaviside_function_2 = 0
    
    S.append(S[i] + dt * (
                            (-beta) * (I[i] + l * J[i]) * S[i] / N 
                          #+ (-beta_star_1) * Heaviside_function_1
                          + (-beta_star_2) * Heaviside_function_2
                          )
            )
    
    E.append(E[i] + dt * (
                            (beta) * (I[i] + l * J[i]) * S[i] / N 
                          #+ (beta_star_1) * Heaviside_function_1
                          + (beta_star_2) * Heaviside_function_2
                          - kappa * E[i]
                          )
            )
    
    I.append(I[i] + dt * (kappa * E[i] - alpha * I[i]))
    
    # J.append(J[i] + dt * (alpha * I[i] - gamma * J[i]))
    J.append(J[i] + dt * (alpha * I[i]))
    # J.append(J[i] + dt * (kappa * E[i]))
    
    R.append(R[i] + dt * gamma * J[i])
    
    t.append(t[i] + dt)

#plt.figure()
# plt.plot(t, S)
# plt.plot(t, E, 'b') # currently exposed MERS but no symptoms
# plt.plot(t, I, 'g') # symptoms; but not confirmed
plt.plot(t, J, 'g') # identified and confirmed; thus, isolated
# plt.plot(t, R, 'r') # cured or deceased
# plt.plot(t, df['일별'], 'o-')
#plt.plot(t, df['누적'], 'o-')
plt.xticks(np.arange(0, 50), labels = day)
plt.legend(['18','11','4'])
#plt.legend(['isolated', 'recoverd', 'daily', 'consum'])
#plt.legend(['modelling','data-accumulation'])
plt.show()

'''
J_1 = [0] * 49

for i in range(len(J_1)):
    J_1[i] = J[i+1] - J[i] 

plt.figure()
# plt.plot(t, I)
plt.plot(t, J_1+[0],'r')
plt.plot(t, df['일별'], 'o-')
# plt.plot(t, [0]*50)
plt.legend(['modelling','data_daily'])
plt.xticks(np.arange(0, 50), 
           labels = day)
plt.show()
'''
'''
plt.figure()
plt.plot(t, df['일별'], 'o-')
plt.xticks(np.arange(0, 50), 
           labels = day)
plt.legend(['daily'])
plt.show()


plt.figure()
plt.plot(t, df['누적'], 'o-')
plt.xticks(np.arange(0, 50), 
           labels = day)
plt.legend(['accumulation'])
plt.show()
'''