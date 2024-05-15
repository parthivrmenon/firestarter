FROM golang:latest

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install any dependencies
RUN go build -o . main

# Command to run the executable
CMD ["./main"]