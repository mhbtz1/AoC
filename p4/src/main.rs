use std::fs::File;
use std::io::BufRead;
use std::vec::Vec;

pub struct Solution;

impl Solution {
    pub fn p1(fpath: &str) -> i64 {
        let input = File::open(fpath).unwrap();
        println!("file path: {}", fpath); // testing ownership semantics
        let reader = std::io::BufReader::new(input);
        let mut map: Vec<Vec<char>> = Vec::new();

        for line in reader.lines() {
            let unwrapped_line = line.unwrap();
            let unwrapped_chars = unwrapped_line.chars().collect::<Vec<_>>();
            map.push(unwrapped_chars);
        }
        let dx: [i64; 8] = [0, 1, 0, -1, 1, 1, -1, -1];
        let dy: [i64; 8] = [1, 0, -1, 0, 1, -1, 1, -1];
        let mut ans = 0;
        for i in 0..map.len() {
            for j in 0..map[i].len() {
                if map[i][j] == 'X' {
                    for k in 0..dx.len() {
                        let mut cx = i64::try_from(i).unwrap(); //char implements Copy, so this obeys ownership semantics
                        let mut cy = i64::try_from(j).unwrap();
                        let char_buf = ['M', 'A', 'S'];
                        let mut idx = 0;
                        while idx < 3 {
                            let signed_len = i64::try_from(map.len()).unwrap();
                            if cx + dx[k] < 0 || cx + dx[k] >= signed_len || cy + dy[k] < 0 || cy + dy[k] >= signed_len {
                                break;
                            }
                            let ucx = usize::try_from(cx + dx[k]).unwrap();
                            let ucy = usize::try_from(cy + dy[k]).unwrap();
                            if map[ucx][ucy] == char_buf[idx] {
                                idx += 1;
                            } else {
                                break;
                            }
                            cx += dx[k];
                            cy += dy[k];
                        }
                        if idx == 3 {
                            ans += 1;
                        }
                    }
                }
            }
        }
        println!("part 1: {}", ans);
        ans
    }    

    pub fn p2(fpath: &str) -> i64 {
        let input = File::open(fpath).unwrap();
        println!("file path: {}", fpath); // testing ownership semantics
        let reader = std::io::BufReader::new(input);
        let mut map: Vec<Vec<char>> = Vec::new();

        for line in reader.lines() {
            let unwrapped_line = line.unwrap();
            let unwrapped_chars = unwrapped_line.chars().collect::<Vec<_>>();
            map.push(unwrapped_chars);
        }
        
        let mut ans = 0;
        for i in 1..map.len()-1 {
            for j in 1..map[i].len()-1 {
                if map[i][j] == 'A' {
                    let dx: [(i64, i64); 2] = [(1, 1), (-1, -1)];
                    let dy: [(i64, i64); 2] = [(1, -1), (-1, 1)];
                    let signed_len = i64::try_from(map.len()).unwrap();
                    for k in 0..dx.len() {
                        let cx = i64::try_from(i).unwrap();
                        let cy = i64::try_from(j).unwrap();
                        let ucx = (i64::try_from(dx[k].0).unwrap(), i64::try_from(dx[k].1).unwrap());
                        if cx + ucx.0 < 0 || cx + ucx.0 >= signed_len || cy + ucx.1 < 0 || cy + ucx.1 >= signed_len {
                            continue;
                        }
                        for l in 0..dy.len() {
                            let ucy = (i64::try_from(dy[l].0).unwrap(), i64::try_from(dy[l].1).unwrap());
                            if cx + ucy.0 < 0 || cx + ucy.0 >= signed_len || cy + ucy.1 < 0 || cy + ucy.1 >= signed_len {
                                continue;
                            }

                            if map[(cx + ucx.0) as usize][(cy + ucx.1) as usize] == 'M' && map[(cx - ucx.0) as usize][(cy - ucx.1) as usize] == 'S' {
                                if map[(cx + ucy.0) as usize][(cy + ucy.1) as usize] == 'M' && map[(cx - ucy.0) as usize][(cy - ucy.1) as usize] == 'S' {
                                    ans += 1;
                                }
                            }
                        }
                    }
                }
            }
        }
        println!("part 2: {}", ans);
        ans
    }    
}

fn main() {
    println!("Hello, world!");
    let args = std::env::args().nth(1).expect("Did not receive a valid command line argument!");
    match args.as_str() {
        "1" => { Solution::p1("src/input.txt"); }
        "2" => { Solution::p2("src/input.txt");}
        _  => { println!("bruh"); }
    }
}
