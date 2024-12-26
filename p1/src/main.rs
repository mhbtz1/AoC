use std::collections::HashMap;
use std::fs;

fn p1() -> i64 {
    let filename = "src/input.txt";
    let binding = fs::read_to_string(filename).expect("ERROR: Could not read file!");
    let contents: Vec<&str> = binding.lines().collect();

    let (left_side, right_side) = (contents.clone(), contents.clone());
    let mut ls = left_side
        .iter()
        .map(|x| {
            let y = x.split_whitespace().collect::<Vec<&str>>();
            return y[0];
        })
        .collect::<Vec<_>>();
    ls.sort();

    let mut rs = right_side
        .iter()
        .map(|x| {
            let y = x.split_whitespace().collect::<Vec<&str>>();
            return y[1];
        })
        .collect::<Vec<_>>();
    rs.sort();

    let mut ans = 0;
    for i in 0..ls.len() {
        println!("left side: {}, right side: {}", ls[i], rs[i]);
        ans += (ls[i].parse::<i64>().unwrap() - rs[i].parse::<i64>().unwrap()).abs();
    }

    return ans;
}

fn p2() -> i64 {
    let filename = "src/input.txt";
    let binding = fs::read_to_string(filename).expect("ERROR: Could not read file!");
    let contents: Vec<&str> = binding.lines().collect();

    let (left_side, right_side) = (contents.clone(), contents.clone());
    let ls = left_side
        .iter()
        .map(|x| {
            let y = x.split_whitespace().collect::<Vec<&str>>();
            return y[0];
        })
        .collect::<Vec<_>>();
    let rs = right_side
        .iter()
        .map(|x| {
            let y = x.split_whitespace().collect::<Vec<&str>>();
            return y[1];
        })
        .collect::<Vec<_>>();
    let mut lfreq: HashMap<&str, i64> = HashMap::new();
    let mut rfreq: HashMap<&str, i64> = HashMap::new();

    for s in ls {
        lfreq.insert(s, lfreq.get(s).unwrap_or(&0) + 1);
    }
    for s in rs {
        rfreq.insert(s, rfreq.get(s).unwrap_or(&0) + 1);
    }

    let mut ans = 0;
    for key in lfreq.keys() {
        ans += key.parse::<i64>().unwrap() * rfreq.get(key).unwrap_or(&0);
    }

    return ans;
}

fn main() {
    let part = std::env::args().nth(1).expect("Did not receive command line argument for part!");
    println!("part: {}", part.clone());
    match part.as_str() {
        "1" => {
            let ans = p1();
            println!("Part 1: {}", ans);
        }
        "2" => {
            let ans = p2();
            println!("Part 2: {}", ans);
        }
        _  => {
            println!("Please enter a valid part number!");
        }
    }
}
