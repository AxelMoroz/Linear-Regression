# Generate random data
set.seed(123)  # for reproducibility
x <- rnorm(100, mean = 50, sd = 10)   # independent variable
y <- 2.5 * x + rnorm(100, mean = 0, sd = 15)  # dependent variable with noise

# Put into a data frame
data <- data.frame(x, y)

# Run linear regression
model <- lm(y ~ x, data = data)

# Summary of the model
summary(model)

# Plot with regression line
plot(data$x, data$y, main="Random Linear Regression in R", 
     xlab="x", ylab="y", pch=19, col="blue")
abline(model, col="red", lwd=2)
