import numpy as np
import math


class Activation():
    def __init__(self, function):
        self.function = function
        self.name = function
        

    def forward(self, Z):
        if self.function == "sigmoid":
            """
            Implements the sigmoid activation in numpy
            
            Arguments:
            Z -- numpy array of any shape
            self.cache -- stores Z as well, useful during backpropagation
            
            Returns:
            A -- output of sigmoid(z), same shape as Z
            
            """

            ### PASTE YOUR CODE HERE ###
            ### START CODE HERE ###

            A = []
            Z = np.array(Z)

            for i in range(Z.shape[0]):
                tmp = []
                for j in range(Z.shape[1]):
                    if Z[i][[j]] >= 0:
                        tmp.append(1 / (1 + math.exp(-Z[i][[j]])))
                    else:
                        tmp.append(math.exp(Z[i][[j]]) / (1 + math.exp(Z[i][[j]])))
                tmp = np.array(tmp)
                A.append(tmp)

            A = np.array(A)

            self.cache = Z

            ### END CODE HERE ###
            
            return A

        elif self.function == "softmax":
            """
            Implements the softmax activation in numpy
            
            Arguments:
            Z -- numpy array of any shape (dim 0: number of classes, dim 1: number of samples)
            self.cache -- stores Z as well, useful during backpropagation
            
            Returns:
            A -- output of softmax(z), same shape as Z
            """

            ### PASTE YOUR CODE HERE ###
            ### START CODE HERE ###

            A = np.exp(Z - np.max(Z)) / sum(np.exp(Z - np.max(Z)))
            self.cache = Z

            ### END CODE HERE ###
            
            return A

        elif self.function == "relu":
            """
            Implement the RELU function in numpy
            Arguments:
            Z -- numpy array of any shape
            self.cache -- stores Z as well, useful during backpropagation
            Returns:
            A -- output of relu(z), same shape as Z
            
            """
            
            ### PASTE YOUR CODE HERE ###
            ### START CODE HERE ###

            A = np.maximum(0, Z)
            self.cache = Z

            ### END CODE HERE ###
            
            assert(A.shape == Z.shape)
            
            return A

    def backward(self, dA=None, Y=None):
        if self.function == "sigmoid":
            """
            Implement the backward propagation for a single SIGMOID unit.
            Arguments:
            dA -- post-activation gradient, of any shape
            self.cache -- 'Z' where we store for computing backward propagation efficiently
            Returns:
            dZ -- Gradient of the cost with respect to Z
            """
            
            ### PASTE YOUR CODE HERE ###
            ### START CODE HERE ###

            Z = self.cache

            A = []
            Z = np.array(Z)
            for i in range(Z.shape[0]):
                tmp = []
                for j in range(Z.shape[1]):
                    val = 0
                    if Z[i][[j]] >= 0:
                        val = 1 / (1 + math.exp(-Z[i][[j]]))
                    else:
                        val = math.exp(Z[i][[j]]) / (1 + math.exp(Z[i][[j]]))
                    tmp.append(val * (1 - val))
                tmp = np.array(tmp)
                A.append(tmp)

            A = np.array(A)
            
            dZ = dA * A

            ### END CODE HERE ###
            
            assert (dZ.shape == Z.shape)
            
            return dZ

        elif self.function == "relu":
            """
            Implement the backward propagation for a single RELU unit.
            Arguments:
            dA -- post-activation gradient, of any shape
            self.cache -- 'Z' where we store for computing backward propagation efficiently
            Returns:
            dZ -- Gradient of the cost with respect to Z
            """
            
            ### PASTE YOUR CODE HERE ###
            ### START CODE HERE ### 

            Z = self.cache
            dZ = dA # just converting dz to a correct object. 
            dZ[Z <= 0] = 0 # When z <= 0, you should set dz to 0 as well.

            ### END CODE HERE ###
            
            assert (dZ.shape == Z.shape)
            
            return dZ

        elif self.function == "softmax":
            """
            Implement the backward propagation for a [SOFTMAX->CCE LOSS] unit.
            Arguments:
            Y -- true "label" vector (one hot vector, for example: [[1], [0], [0]] represents rock, [[0], [1], [0]] represents paper, [[0], [0], [1]] represents scissors 
                                      in a Rock-Paper-Scissors image classification), shape (number of classes, number of examples)
            self.cache -- 'Z' where we store for computing backward propagation efficiently
            Returns:
            dZ -- Gradient of the cost with respect to Z
            """
            
            ### PASTE YOUR CODE HERE ###
            ### START CODE HERE ### 

            Z = self.cache
            s = np.exp(Z) / sum(np.exp(Z))
            dZ = s - Y

            ### END CODE HERE ###
            
            assert (dZ.shape == Z.shape)
            
            return dZ
