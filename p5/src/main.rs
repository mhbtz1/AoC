
use std::{collections::{HashSet, HashMap}, fs};
use std::vec::Vec;
use std::str::FromStr;

pub struct Solution;

type Node = u64;
pub type Graph = HashMap<Node, Vec<Node>>;
static default: Vec<Node> = Vec::new();

impl<'a> Solution {

    pub fn kahn(g: &'a Graph, ordering: &'a Vec<Node>, start: Option<&'a Node>) -> (bool, Vec<&'a Node>) {
        let mut queue = Vec::new();
        queue.push((ordering[0], 0) );
        let mut vis = HashSet::new();
        let mut valid = false;

        while queue.len() > 0 {
            let front = queue.pop().unwrap();
            let nbrs: &Vec<Node> = &g.get(&front.0).unwrap_or(&default);
            vis.insert(front);
            if front.1 == ordering.len() - 1 {
                valid = true;
            }
            for nbr in nbrs {
                if vis.contains(&(*nbr, front.1+1) ) {
                    continue;
                }
                if front.1 + 1 < ordering.len() && ordering[front.1 + 1] == *nbr {
                    queue.push( (*nbr, front.1 + 1) );
                }
            }
        }
    
        let mut reorder_nodes: Vec<&Node> = Vec::new();
        let mut vis = HashSet::new();
        if start.is_some() {
            let mut second_queue: Vec<(&'a Node, Vec<&Node>)> = Vec::new();
            second_queue.push( (start.unwrap(), vec![start.unwrap()]) ); 
            reorder_nodes.push(start.unwrap());
        
            while second_queue.len() > 0 {
                let front = second_queue.pop().unwrap();
                vis.insert(front.clone());
                //println!("current node: {:?}, current path: {:?}", front.0, &front.1);
                if front.1.len() == ordering.len() {
                    reorder_nodes = front.1.clone();
                    break;
                }

                let nbrs: &Vec<Node> = &g.get(front.0).unwrap_or(&default);
                
                for nbr in nbrs { // nbr is type &Node
                    let mut prev = front.1.clone();
                    prev.push(nbr);
                    if !vis.contains(&(nbr, prev.clone()) ) && (g[&front.1[front.1.len()-1]].iter().any(|item| std::ptr::eq(item, nbr))) && ordering.contains(nbr) {
                        let mut prev = front.1.clone();
                        prev.push(nbr);
                        second_queue.push( (nbr, prev.clone()) );
                    } else {
                        //println!("result: {}", g[&front.1[front.1.len()-1]].iter().any(|item| std::ptr::eq(item, nbr)));
                    }
                }
            }
        }

        return (valid, reorder_nodes);
    }


    pub fn p1(fpath: &str) -> u64 {
        //println!("file path: {}", fpath); // testing ownership semantics
        let fcontent = fs::read_to_string(fpath).expect("not able to read file!");
        let vec = fcontent.split("\n\n").collect::<Vec<_>>();
        
        let mut ordering = vec[0].split('\n').into_iter().collect::<Vec<&str>>();
        let mut g: Graph = HashMap::new();
        let mut nodes: HashSet<u64> = HashSet::new();
        
        let mut start_node: u64 = 12;
        for order in ordering {
            let left = u64::from_str(&order[0..order.find("|").unwrap() ]).unwrap();
            let right = u64::from_str(&order[order.find("|").unwrap()+1..]).unwrap();
            g.entry(left).or_insert_with(Vec::new).push(right);
            nodes.insert(left);
            nodes.insert(right);
        }

        //println!("number of nodes in graph: {}", g.keys().len());
        let updates = vec[1].split("\n").into_iter().collect::<Vec<&str>>();
        let mut ans = 0;
        for update in &updates {
            let mut ordering = update.split(",").collect::<Vec<&str>>().into_iter().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();
            let (valid, _) = Solution::kahn(&g, &mut ordering, None);
            if valid {
                ans += ordering[ordering.len() / 2];
            }
        }
        //println!("part 1: {}", ans);
        ans
    }  


    pub fn p2(fpath: &str) -> u64 {
        //println!("file path: {}", fpath); // testing ownership semantics
        let fcontent = fs::read_to_string(fpath).expect("not able to read file!");
        let vec = fcontent.split("\n\n").collect::<Vec<_>>();
        
        let mut ordering = vec[0].split('\n').into_iter().collect::<Vec<&str>>();
        let mut g: Graph = HashMap::new();
        
        for order in ordering {
            let left = u64::from_str(&order[0..order.find("|").unwrap() ]).unwrap();
            let right = u64::from_str(&order[order.find("|").unwrap()+1..]).unwrap();
            g.entry(left).or_insert_with(Vec::new).push(right);
        }


        let updates = vec[1].split("\n").into_iter().collect::<Vec<&str>>();
        let mut ans = 0;
        for update in &updates {
            let mut ordering = update.split(",").collect::<Vec<&str>>().into_iter().map(|x| x.parse::<u64>().unwrap()).collect::<Vec<u64>>();
            let mut setcoll: HashSet<Node> = ordering.clone().into_iter().collect::<HashSet<_>>();

            let cln = ordering.clone();
            for start in &cln {
                let (valid, reordered_nodes) = Solution::kahn(&g, &ordering, Some(start));
                if valid {
                    break;
                } else {
                    if reordered_nodes.len() == cln.len() {
                        ans += reordered_nodes[reordered_nodes.len() / 2];
                        //println!("reordered: {:?}", &reordered_nodes);
                        break;
                    } else {
                        //println!("reordered len: {}, cln len: {}", reordered_nodes.len(), cln.len());
                    }
                }
                setcoll = ordering.clone().into_iter().collect::<HashSet<_>>();
            }
        }
        println!("part 2: {}", ans);
        return ans;
    }    

}


fn main() {
    //println!("Hello, world!");
    Solution::p2("src/smol_input.txt");
}
