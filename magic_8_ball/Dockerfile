FROM golang:latest

# Set the working directory in the container
WORKDIR /app

# Copy the local code to the container
COPY . /app

# Install any dependencies
RUN go build -o .

# Command to run the executable
CMD ["./magic_8_ball_app"]