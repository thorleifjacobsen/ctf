#[macro_use] extern crate rocket;

use std::cmp::min;

use rocket::fs::NamedFile;
use rocket::fs::FileServer;
use rocket::response::status::BadRequest;

mod image_from_request_body;
use crate::image_from_request_body::ImageData;

use magick_rust::{bindings, magick_wand_genesis, MagickWand};

#[get("/")]
async fn index() -> Result<NamedFile, std::io::Error> {
    NamedFile::open("static/index.html").await
}

#[post("/resize?<x>&<y>", data="<image>")]
fn resize(image: ImageData, x: Option<u16>, y: Option<u16>) -> Result<Vec<u8>, BadRequest<String>> {
    let max_size = 1024;
    let default_size = 32;
    let size_x = min(x.unwrap_or(default_size), max_size);
    let size_y = min(y.unwrap_or(default_size), max_size);
    let wand = MagickWand::new();
    let _ = wand.read_image_blob(&image.data);
    wand.resize_image(size_x.into(), size_y.into(), bindings::FilterType_LanczosFilter);
    match wand.write_image_blob("PNG") {
        Ok(vec) => Ok(vec),
        Err(_) => Err(BadRequest("couldn't convert provided image".into())) // might be our problem, but blame the user anyway
    }
}

#[launch]
fn rocket() -> _ {
    magick_wand_genesis();
    rocket::build()
        .mount("/", routes![index, resize])
        .mount("/static", FileServer::from("static"))
}
