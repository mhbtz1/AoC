
use std::{collections::{HashSet, HashMap}, fs};
use std::vec::Vec;
use std::str::FromStr;

pub struct Solution;

type Node = u64;
pub type Graph = HashMap<Node, Vec<Node>>;

impl Solution {

    pub fn kahn(g: &Graph, start: Node, indegrees: &mut HashMap<Node, u64>) -> Vec<Node> {
        let mut queue = Vec::new();
        queue.push(start);
        let mut topo_order = Vec::new();
        let mut ptr = 0;
        let mut vis = HashSet::new();
        while queue.len() > 0 {
            let front = queue.pop().unwrap();
            topo_order.push(front.clone());
            let default = Vec::new();
            let nbrs: &Vec<Node> = &g.get(&front).unwrap_or(&default);
            vis.insert(front);
            for nbr in nbrs {
                if vis.contains(nbr) {
                    continue;
                }
                if *indegrees.get(nbr).unwrap() == 0 {
                    queue.push(*nbr);
                    continue;
                }
                indegrees.insert(*nbr, *indegrees.get(nbr).unwrap_or(&1) - 1);
                if *indegrees.get(nbr).unwrap() == 0 {
                    queue.push(*nbr);
                }
            }
        }

        println!("topo order: {:?}", topo_order);
        topo_order
    }

    pub fn p1(fpath: &str) -> u64 {
        println!("file path: {}", fpath); // testing ownership semantics
        let fcontent = fs::read_to_string("src/input.txt").expect("not able to read file!");
        let vec = fcontent.split("\n\n").collect::<Vec<_>>();
        
        let mut ordering = vec[0].split('\n').into_iter().collect::<Vec<&str>>();
        let mut indegree: HashMap<u64, u64> = HashMap::new();
        let mut g: Graph = HashMap::new();
        let mut nodes: HashSet<u64> = HashSet::new();
        
        let mut start_node: u64 = 0;
        for order in ordering {
            let left = u64::from_str(&order[0..order.find("|").unwrap() ]).unwrap();
            let right = u64::from_str(&order[order.find("|").unwrap()+1..]).unwrap();
            indegree.insert(right, indegree.get(&right).unwrap_or(&0) + 1);
            g.entry(left).or_insert_with(Vec::new).push(right);
            nodes.insert(left);
            nodes.insert(right);
        }
        for node in nodes {
            if *indegree.get(&node).unwrap_or(&0) == 0 {
                start_node = node;
                break;
            }
        } 
        

        let updates = vec[1].split("\n").into_iter().collect::<Vec<&str>>();
        let topo_ordering = Solution::kahn(&g, start_node, &mut indegree);
        let mut ans = 0;
        for update in &updates {
            let mut ordering = update.split(",").collect::<Vec<&str>>().into_iter().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();
            let mut ptr = 0;
            for value in &topo_ordering {
                if ptr < ordering.len() && ordering[ptr] == *value {
                    ptr += 1;
                }
            }
            if ptr == ordering.len() {
                ans += ordering[ordering.len() / 2];
            }
        }
        println!("part 1: {}", ans);
        ans
        
    }  


    pub fn p2(fpath: &str) -> i64 {
        -1
    }    

}


fn main() {
    println!("Hello, world!");
    Solution::p1("src/input.txt");
}
