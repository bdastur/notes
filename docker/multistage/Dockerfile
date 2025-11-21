# Stage 1: Build the application
FROM golang:1.22 AS builder
WORKDIR /app
COPY /app .
RUN go mod init myapp

 
#RUN CGO_ENABLED=0 GOARCH=arm64 GOOS=darwin go build -a -installsuffix cgo -o myapp .
RUN go build -a -installsuffix cgo -o myapp .
RUN ls -l /
RUN ls -l /app
RUN echo "End"

# Stage 2: Create the distroless image
FROM golang:1.22
#FROM gcr.io/distroless/static-debian12
RUN ls -l /
COPY  --from=builder /app/myapp myapp
#USER nonroot:nonroot
ENTRYPOINT ["./myapp"]

