mod select_units;

fn welcome(version: &str) {
    println!("convert_unit version {}", version);
}

fn main() {
    let current_version = "0.0.0";
    welcome(current_version);
    println!("Please enter the unit you wish to convert from: [mi, nmi, km, m, mi_uss]");
    select_units::request_units();
}
