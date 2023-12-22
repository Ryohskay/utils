fn main() {
    println!("This is a programme to convert Earth coordinate degrees in decimal into minutes and seconds.");
    println!("Please enter the latitude to convert: ");

    let mut latitude = String::new();

    std::io::stdin()
        .read_line(&mut latitude)
        .expect("Failed to read line!");

    // trimming is vital. without this it causes an runtime error due to newline char at the end.
    let f_lat: f32 = latitude.trim().parse().expect("failed parsing into f32!");
    println!("Latitude was: {f_lat}");

    let lat_int_part: f32 = f_lat.trunc();  // integer part of the float latitude.
    let lat_decimal_part = f_lat.fract();  // the decimal part of the latitude.

    let lat_fract_in_sec: f32 = 3600.0 * lat_decimal_part;  // the decimal part expressed in seconds
    let lat_min: f32 = (lat_fract_in_sec / 60.0).trunc();  // values under decimal is treated in seconds
    let lat_sec: f32 = (lat_fract_in_sec % 60.0).round(); // rounds to nearest integer = seconds.

    print_deg(f_lat, lat_int_part, lat_min, lat_sec);

}

fn print_deg(decimal: f32, deg: f32, min: f32, sec: f32) {
    let hemisphere: String;
    
    if decimal.is_normal() {
        println!("WARNING: The original input decimal value is not normal.");
    }
    
    if decimal.is_sign_positive() {
        hemisphere = "N".to_string();
    } else {
        hemisphere = "S".to_string();
    }

    println!("The decimal latitude of {decimal} was converted to: ");
    println!("Latitude: {}° {}\' {}\" {}", deg.abs(), min.abs(), sec.abs(), hemisphere);
}
