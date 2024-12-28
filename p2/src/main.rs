use std::fs;

fn validate(arr: Vec<i64>) -> bool{
    let mut cur = arr[1];
    let relation : bool = match arr[0] < cur { 
                            true => true,
                            false => false      
                          };
    let mut valid = (cur - arr[0]).abs() >= 1 && (cur - arr[0]).abs() <= 3;
    for i in 2..arr.len() {
        if ((relation && cur < arr[i]) || (!relation && cur >= arr[i])) && ((cur - arr[i]).abs() >= 1 && (cur - arr[i]).abs() <= 3) {
            cur = arr[i];
        } else {
            valid = false;
            break;
        }
    }
    valid
}

fn p1(input_str: &str) -> i64 {
    let binding = fs::read_to_string(input_str).expect("ERROR: Could not read file!");
    // recall: str denotes an immutable sequence of UTF-8 bytes, String is a pointer to a heap-allocated sequence of UTF-8 bytes (i.e. can be dynamically grown)
    // also: recall that 
    let contents: Vec<&str> = binding.lines().collect();
    let mut ans = 0;

    for content in contents {
        let arr = content.split(" ").collect::<Vec<_>>().into_iter().map(|x| x.parse::<i64>().unwrap()).collect::<Vec<i64>>();
        println!("arr: {:?}", arr);
        let valid = validate(arr);
        if valid {
            ans += 1;
        }
    }
    ans

}

fn p2(input_str: &str) -> i64 {
    let binding = fs::read_to_string(input_str).expect("ERROR: Could not read file!");
    // recall: str denotes an immutable sequence of UTF-8 bytes, String is a pointer to a heap-allocated sequence of UTF-8 bytes (i.e. can be dynamically grown)
    // also: recall that 
    let contents: Vec<&str> = binding.lines().collect();
    let mut ans = 0;
    for content in contents {
        let mut arr = content.split(" ").collect::<Vec<_>>().into_iter().map(|x| x.parse::<i64>().unwrap()).collect::<Vec<i64>>();
        for rem in 0..arr.len() {
            let val = arr[rem];
            arr.remove(rem);
            let valid = validate(arr.clone());
            if valid {
                ans += 1;
                break;
            }
            arr.insert(rem, val);
        }
    }
    ans
} 


fn main() {
    let part = std::env::args().nth(1).expect("Did not receive command line argument for part!");
    match part.as_str() {
        "1" => {let ans = p1("src/input.txt"); println!("part 1: {}", ans);}
        "2" => {let ans = p2("src/input.txt"); println!("part 2: {}", ans);}
        _ => { println!("Invalid part!"); }
    }
}
