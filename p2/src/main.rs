fn p1(input_str: &str) -> i64 {
    let binding = fs::read_to_string(input_str).expect("ERROR: Could not read file!");
    // recall: str denotes an immutable sequence of UTF-8 bytes, String is a pointer to a heap-allocated sequence of UTF-8 bytes (i.e. can be dynamically grown)
    let contents: Vec<&str> = binding.lines().collect();
    let mut ans = 0;

    for content in contents {
        let arr = contents.split(" ").collect::<Vec<&str>>();
        let cur = arr[1];
        let relation = if (arr[0] < cur) { 1 } else {0 };
        let valid = true;
        for i in 2..arr.len() {
            if (relation && cur < arr[i]) || (!relation && cur > arr[i]) {
                cur = arr[i];
            } else {
                valid = false;
                break;
            }
        }
        if valid {
            ans += 1;
        }
    }

    return ans;

}


fn main() {
    let part = std::env::args().nth(1).expect("Did not receive command line argument for part!");
    match part.as_str() {
        "1" => {let ans = p1("src/input.txt"); println!("part 1: {}", ans);},
        "2" => {let ans = p2("src/input.txt"); println!("part 2: {}", ans);}
    }
}
