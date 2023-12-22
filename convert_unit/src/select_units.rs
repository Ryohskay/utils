mod distance_units;

fn select_unit(unit: &str) -> Result<i32, &'static str> {
    let id: i32;
    match unit {
        "mi" => id = 1,
        "nmi" => id = 2,
        "km" => id = 3,
        "m" => id = 4,
        "mi_uss" => id = 5,
        _ => return Err("No matching unit found"),
    }
    return Ok(id);
}

pub fn request_units() {
    let mut selected_unit_id: i32 = 0;
    let unit_name: String;

    for n in 0..20 {
        let mut original_unit = String::new();
        std::io::stdin()
            .read_line(&mut original_unit)
            .expect("Failed to read line!");

        let original_unit: &str = original_unit.trim(); // transformed into &str type
        println!("The input was: {original_unit}");

        if !((1..=5).contains(&selected_unit_id)) {
            let selection_res = select_unit(&original_unit);

            match selection_res {
                Ok(id) => {
                    selected_unit_id = id;
                    break;
                }
                Err(s) => println!("Error: {s} - Please try again."),
            }

            if n == 19 {
                println!("Something went wrong; tried {n} times, but could not find matching unit {original_unit}. 
                    Please restart the programme and try again.");
                std::process::exit(1);
            }
        }
    }

    match selected_unit_id {
        1 => unit_name = String::from("mile (international)"),
        2 => unit_name = String::from("nautical mile (international)"),
        3 => unit_name = String::from("kilometre"),
        4 => unit_name = String::from("metre"),
        5 => unit_name = String::from("US Survey Mile"),
        _ => {
            println!("Something went wrong!");
            std::process::exit(1);
        } // selected_unit_id must be one of the above. If any other value was found, the value is broken.
    }

    println!("Your choice was parsed as: {selected_unit_id} - {unit_name}");
}
