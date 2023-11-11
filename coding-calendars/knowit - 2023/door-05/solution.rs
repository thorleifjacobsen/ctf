use std::convert::TryInto;

// Check if number is prime
fn is_prime(num: u64) -> bool {
    if num < 2 {
        return false;
    }

    if num <= 3 {
        return true;
    }

    if num % 2 == 0 || num % 3 == 0 {
        return false;
    }

    let mut i = 5;
    while i * i <= num {
        if num % i == 0 || num % (i + 2) == 0 {
            return false;
        }
        i += 6;
    }

    true
}

fn sum_of_digits(mut num: u64) -> u64 {
    let mut sum = 0;

    while num > 0 {
        sum += num % 10;
        num /= 10;
    }

    sum
}

// Criterias: sum of digits, divided by sum, is whole number, is prime
fn is_sum_divide_prime(num: u64) -> bool {
    if num < 2 {
        return false;
    }

    let sum = sum_of_digits(num);

    if sum <= 1 {
        return false;
    }

    let divided_by_sum = num as f64 / sum as f64;
    divided_by_sum.fract() == 0.0 && is_prime(divided_by_sum as u64)
}



fn main() {
    let mut sum_divide_primes = 0;

    for i in 1..=100000000 {
        if is_sum_divide_prime(i as u64) {
            sum_divide_primes += 1;
        }
    }

    println!("{}", sum_divide_primes);
}