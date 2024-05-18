use std::io;

fn no_more_case() {
    println!("Too bad so sad");
    return;
}

fn million_dollars(input: String) {
    let firstchar = input.trim().chars().next().unwrap_or('\0');

    if firstchar == '}' {
        println!("You won the million dollars!!!");
    }
    else {
        println!("You were so close...");
    }
}

// [('b', 98), ('y', 121), ('u', 117), ('C', 67), ('T', 84), ('F', 70), ('{', 123), ('y', 121), ('0', 48), 
// ('u', 117), ('_', 95), ('c', 99), ('A', 65), ('n', 110), ('_', 95), ('u', 117), ('S', 83), ('3', 51), 
// ('_', 95), ('r', 114), ('u', 117), ('s', 115), ('t', 116), ('!', 33), ('}', 125)]

fn briefcase_no_1(input: String, no: u32) {
    println!("You're opening the first briefcase!");

    let firstchar = input.trim().chars().next().unwrap_or('\0');

    let rest_of_string = input.chars().skip(1).collect();

    if firstchar == 'u' && no == 3 {
        briefcase_no_4(rest_of_string, 1);
    }
    else if firstchar == '!' && no == 2 {
        million_dollars(rest_of_string);
    }
    else if firstchar == '0' && no == 5 {
        briefcase_no_2(rest_of_string, 1);
    }
    else if firstchar == 'b' && no == 0 {
        briefcase_no_3(rest_of_string, 1);
    }
    else {
        no_more_case();
    }
    

    // match firstchar as u8 {
    //     //98 => briefcase_no_3(rest_of_string),
    //     //48 => briefcase_no_2(rest_of_string),
    //     //117 => briefcase_no_4(rest_of_string),
    //     //33 => million_dollars(rest_of_string),
    //     _ => no_more_case()
    // };
}

fn briefcase_no_2(input: String, no: u32) {
    println!("You're opening the second briefcase!");

    let firstchar = input.trim().chars().next().unwrap_or('\0');

    let rest_of_string = input.chars().skip(1).collect();

    if firstchar == 't' && no == 4 {
        briefcase_no_1(rest_of_string, 2);
    }
    else if firstchar == 'u' && no == 3 {
        briefcase_no_2(rest_of_string, 2);
    }
    else if firstchar == '_' && no == 2 {
        briefcase_no_3(rest_of_string, 2);
    }
    else if firstchar == 'c' && no == 2 {
        briefcase_no_4(rest_of_string, 2);
    }
    else if firstchar == 'u' && no == 1 {
        briefcase_no_2(rest_of_string, 2);
    }
    else if firstchar == '_' && no == 5 {
        briefcase_no_3(rest_of_string, 2);
    }
    else {
        no_more_case();
    }
    

    // match firstchar as u8 {
    //     //117 => briefcase_no_2(rest_of_string),
    //     //67 => briefcase_no_4(rest_of_string),
    //     //95 => briefcase_no_3(rest_of_string),
    //     //116 => briefcase_no_1(rest_of_string),
    //     _ => no_more_case()
    // };
}

fn briefcase_no_3(input: String, no: u32) {
    println!("You're opening the third briefcase!");

    let firstchar = input.trim().chars().next().unwrap_or('\0');

    let rest_of_string = input.chars().skip(1).collect();

    if firstchar == 'y' && no == 1 {
        briefcase_no_2(rest_of_string, 3);
    }
    else if firstchar == 'f' && no == 4 {
        briefcase_no_5(rest_of_string, 3);
    }
    else if firstchar == 'c' && no == 2 {
        briefcase_no_5(rest_of_string, 3);
    }
    else if firstchar == '_' && no == 4 {
        briefcase_no_1(rest_of_string, 3);
    }
    else if firstchar == 'r' && no == 2 {
        briefcase_no_1(rest_of_string, 3);
    }
    else {
        no_more_case();
    }

    // match firstchar as u8 {
    //     //121 => briefcase_no_2(rest_of_string),
    //     //70 => briefcase_no_5(rest_of_string),
    //     //95 => briefcase_no_1(rest_of_string),
    //     //99 => briefcase_no_5(rest_of_string),
    //     //114 => briefcase_no_1(rest_of_string),
    //     _ => no_more_case()
    // };
}

fn briefcase_no_4(input: String, no: u32) {
    println!("You're opening the fourth briefcase!");

    let firstchar = input.trim().chars().next().unwrap_or('\0');

    let rest_of_string = input.chars().skip(1).collect();

    if firstchar == 't' && no == 2 {
        briefcase_no_3(rest_of_string, 4);
    }
    else if firstchar == 'n' && no == 5 {
        briefcase_no_3(rest_of_string, 4);
    }
    else if firstchar == 'S' && no == 1 {
        briefcase_no_5(rest_of_string, 4);
    }
    else if firstchar == 's' && no == 1 {
        briefcase_no_2(rest_of_string, 4);
    }
    else {
        no_more_case();
    }

    // match firstchar as u8 {
    //     //84 => briefcase_no_3(rest_of_string),
    //     //110 => briefcase_no_3(rest_of_string),
    //     //83 => briefcase_no_5(rest_of_string),
    //     115 => briefcase_no_2(rest_of_string),
    //     _ => no_more_case()
    // };
}

fn briefcase_no_5(input: String, no: u32) {
    println!("You're opening the fifth briefcase!");

    let firstchar = input.trim().chars().next().unwrap_or('\0');

    let rest_of_string = input.chars().skip(1).collect();

    if firstchar == '{' && no == 3 {
        briefcase_no_5(rest_of_string, 5);
    }
    else if firstchar == 'y' && no == 5 {
        briefcase_no_1(rest_of_string, 5);
    }
    else if firstchar == 'A' && no == 3 {
        briefcase_no_4(rest_of_string, 5);
    }
    else if firstchar == '3' && no == 4 {
        briefcase_no_2(rest_of_string, 5);
    }
    else {
        no_more_case();
    }

    // match firstchar as u8 {
    //     //123 => briefcase_no_5(rest_of_string),
    //     //121 => briefcase_no_1(rest_of_string),
    //     //65 => briefcase_no_4(rest_of_string),
    //     //51 => briefcase_no_2(rest_of_string),
    //     _ => no_more_case()
    // };
}

fn main() {
    let mut input = String::new();

    io::stdin().read_line(&mut input)
        .expect("Failed to read line");

    let numchars = input.chars().count();
    if numchars != 26 {
        println!("Too bad so sad");
        return;
    }

    briefcase_no_1(input, 0);
}

