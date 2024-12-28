use std::fs::File;
use std::io::BufRead;
use regex::Regex;

fn p1(input_file: &str) -> i64 {
    let input = File::open(input_file).unwrap();
    let reader = std::io::BufReader::new(input);
    let mut ans : i64 = 0;
    let pattern = Regex::new(r"mul\((-?\d+),(-?\d+)\)").unwrap();
    for line in reader.lines() {
        let unwrapped_line = line.unwrap();
        let all_matches = pattern.captures_iter(&unwrapped_line.as_str());
        for mtch in all_matches {
            let x = mtch[1].parse::<i64>().unwrap();
            let y = mtch[2].parse::<i64>().unwrap();
            println!("x: {}, y: {}", x, y);
            ans += x * y;
        }
    }
    println!("part 1: {}", ans);
    ans
}

fn p2(input_file: &str) -> i64 {
    let input = File::open(input_file).unwrap();
    let reader = std::io::BufReader::new(input);
    let mut ans : i64 = 0;
    let pattern = Regex::new(r"mul\((-?\d+),(-?\d+)\)").unwrap();
    let do_pattern = Regex::new("do()").unwrap();
    let dont_pattern = Regex::new("don't()").unwrap();

    let mut used = true;
    
    for line in reader.lines() {
        let unwrapped_line = line.unwrap();
        let unwrapped_chars = unwrapped_line.chars().collect::<Vec<_>>();
        let mut i = 0;
        while i < unwrapped_chars.len(){
            if i <= unwrapped_chars.len()-7 && unwrapped_chars[i..i+7] == ['d', 'o', 'n', '\'', 't', '(', ')'] {
                used = false;
            }
            if i <= unwrapped_chars.len()-4 && unwrapped_chars[i..i+4] == ['d', 'o', '(', ')'] {
                used = true;
            }
            

            if used && i < unwrapped_chars.len()-2 && unwrapped_chars[i..i+3] == ['m', 'u', 'l'] {
                if unwrapped_chars[i+3] == '(' {
                    let mut lstr = String::new();
                    let mut rstr = String::new();
                    let mut mode = 0;
                    let mut j = i+4;
                    let mut valid = true;
                    while j < unwrapped_chars.len() && unwrapped_chars[j] != ')' {
                        if unwrapped_chars[j] == ',' {
                            mode = 1;
                        } 
                        
                        if unwrapped_chars[j] != ',' {
                            if !unwrapped_chars[j].is_numeric() {
                                valid = false;
                                break;
                            }
                            if mode == 0 {
                                lstr.push(unwrapped_chars[j]);
                            } else {
                                rstr.push(unwrapped_chars[j]);
                            }
                        }

                        j += 1;
                    }
                    if valid {
                        let x = lstr.parse::<i64>().unwrap_or(0);
                        let y = rstr.parse::<i64>().unwrap_or(0);
                        ans += x * y;
                    }
                    i = j;
                }
            }
            i += 1;
        }
    }
    println!("part 2: {}", ans);
    ans
}

fn main() {
    let args = std::env::args().nth(1).expect("Did not receive command line argument for part!");
    match args.as_str() {
        "1" => { p1("src/input.txt"); }
        "2" => { p2("src/input.txt"); }
        _ => { println!("Pattern is not covered!"); }
    }
}