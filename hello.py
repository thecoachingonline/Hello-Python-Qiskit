from qiskit import QuantumCircuit, Aer, execute

# Create a quantum circuit with one qubit
circuit = QuantumCircuit(1, 1)

# Apply the X gate (NOT gate) to the qubit
circuit.x(0)

# Measure the qubit and store the result in a classical bit
circuit.measure(0, 0)

# Simulate the circuit using the Qiskit Aer simulator
backend = Aer.get_backend('qasm_simulator')
job = execute(circuit, backend)
result = job.result()

# Print the result of the simulation
counts = result.get_counts()
print(counts)
