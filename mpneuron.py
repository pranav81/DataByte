class MPNeuron:

    def __init__(self):
        self.n = 3
        self.inputs = [1,1,1]
        self.weights = [1,1,1]
        self.t = 2.5


    def MP_Neuron_Input(self):
        self.n = int(input('Enter the number of inputs: '))
        self.inputs = list(map(int, (input('Enter comma separated inputs: ').split(','))))
        self.weights = list(map(int, (input('Enter comma separated weights (+1 singnifies excitatory and -1 signifies inhibitory): ').split(','))))
        self.t = int(input('Enter the threshold: '))


    def MP_Neuron_Evaluate(self):
        sum = 0
        for i in range(self.n):
            sum = sum + (self.inputs[i]*self.weights[i])
        if sum<self.t:
            return 0
        else:
            return 1

'''test = MPNeuron()

test.MP_Neuron_Input()

result = test.MP_Neuron_Evaluate()
print(result)'''

''' 3-input NAND '''

print('Input 1')

number1 = MPNeuron()

number1.MP_Neuron_Input()

result1 = number1.MP_Neuron_Evaluate()

print('Result 1: ', result1)

print('Input 2')

number2 = MPNeuron()

number2.MP_Neuron_Input()

result2 = number2.MP_Neuron_Evaluate()

print('Result 2: ', result2)


print('Input 3')

number3 = MPNeuron()

number3.MP_Neuron_Input()

result3 = number3.MP_Neuron_Evaluate()

print('Result 3: ', result3)


print('NAND')

nand = MPNeuron()

nand.MP_Neuron_Input()

nand_result = nand.MP_Neuron_Evaluate()

print('NAND Result: ', nand_result)
