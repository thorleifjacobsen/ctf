use rocket::request:: Request;
use rocket::data::{self, Data, FromData, ToByteUnit};
use rocket::http::{Status, ContentType};
use rocket::outcome::Outcome;

#[derive(Debug)]
pub enum Error {
    TooLarge,
    Io(std::io::Error),
}

pub struct ImageData {
    pub data: Vec<u8>
}

#[rocket::async_trait]
impl<'r> FromData<'r> for ImageData {
    type Error = Error;

    async fn from_data(req: &'r Request<'_>, data: Data<'r>) -> data::Outcome<'r, Self> {
        use Error::*;

        let png_ct = ContentType::new("image", "png");
        let jpg_ct = ContentType::new("image", "jpeg");
        if req.content_type() != Some(&png_ct) && req.content_type() != Some(&jpg_ct) {
            return Outcome::Forward((data, Status::UnsupportedMediaType));
        }
        
        let limit = req.limits().get("file").unwrap_or(2048.bytes());

        let img_data = match data.open(limit).into_bytes().await {
            Ok(img_data) if img_data.is_complete() => img_data.into_inner(),
            Ok(_) => return Outcome::Error((Status::PayloadTooLarge, TooLarge)),
            Err(e) => return Outcome::Error((Status::InternalServerError, Io(e))),
        };
        Outcome::Success(ImageData {data: img_data})
    }
}
