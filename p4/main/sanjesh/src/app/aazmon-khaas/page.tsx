"use client";
import { FormEvent, useRef, useState } from "react";
import TextareaAutosize from "react-textarea-autosize";

import { FaImage, FaCalendar } from "react-icons/fa";
import Link from "next/link";

export default function page() {
  const address = useRef<HTMLTextAreaElement>(null);

  const firstName = useRef<HTMLInputElement>(null);
  const lastName = useRef<HTMLInputElement>(null);
  const fatherName = useRef<HTMLInputElement>(null);
  const mahalTavalod = useRef<HTMLInputElement>(null);
  const shShenasname = useRef<HTMLInputElement>(null);
  const shMelli = useRef<HTMLInputElement>(null);
  const tavalod = useRef<HTMLInputElement>(null);
  const phone = useRef<HTMLInputElement>(null);
  const telPhone = useRef<HTMLInputElement>(null);
  const email = useRef<HTMLInputElement>(null);

  const [pictureFile, setpictureFile] = useState<File | null>(null);

  const [sabtnaam, setSabtnaam] = useState<boolean>(false);

  const submitHandle = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setSabtnaam(true);
  };

  // /////////////////////////////
  const [createObjectURL, setCreateObjectURL] = useState<any>(null);

  const uploadToClient = (event: any) => {
    if (event.target.files && event.target.files[0]) {
      const i = event.target.files[0];
      setCreateObjectURL(URL.createObjectURL(i));
      setpictureFile(event.target.files[0].name);
    }
  };

  return (
    <div className="page form-section">
      <h2>
        {!sabtnaam && "Aazmoone khaas"}
        {sabtnaam && "Etelaat Shoma"}
      </h2>
      {!sabtnaam && (
        <form
          action=""
          className="my-form"
          autoComplete="off"
          onSubmit={submitHandle}
        >
          <div className="two">
            <input
              required
              ref={firstName}
              className="input"
              type="text"
              id="first-name"
              placeholder="Naam"
            />
            <input
              required
              ref={lastName}
              className="input"
              type="text"
              id="last-name"
              placeholder="Naam khaanevadegi"
            />
          </div>
          <div className="two">
            <input
              required
              ref={fatherName}
              className="input"
              type="text"
              id="father-name"
              placeholder="Naam pedar"
            />
            <input
              required
              ref={mahalTavalod}
              className="input"
              type="text"
              id="mahal-tavalod"
              placeholder="Mahal tavalod"
            />
          </div>

          <div className="two">
            <input
              required
              ref={shShenasname}
              className="input"
              type="text"
              id="sh-shenasname"
              placeholder="Shomare Shenasname"
            />
            <input
              required
              ref={shMelli}
              className="input"
              type="text"
              id="sh-melli"
              placeholder="Shomare melli"
            />
          </div>

          <span>Taarikh tavalod:</span>
          <input
            required
            ref={tavalod}
            className="input"
            type="date"
            name=""
            id="tavalod"
          />

          <TextareaAutosize
            required
            ref={address}
            className="input"
            minRows={3}
            autoComplete="off"
            // ref={blogText}
            id="text"
            placeholder="Address"
            // disabled={disableForm}
          />
          <input
            required
            ref={phone}
            className="input"
            type="text"
            id="phone"
            placeholder="Phone"
          />
          <input
            required
            ref={telPhone}
            className="input"
            type="text"
            id="telphone"
            placeholder="Telephone hamraah"
          />

          <input
            required
            ref={email}
            className="input"
            type="email"
            name=""
            id="email"
            placeholder="Email"
          />
          <span>Aks:</span>
          <label
            htmlFor="img-file"
            className="custom-input flex input text-white"
          >
            {!createObjectURL && "Akse khod ra upload konid"}
            {createObjectURL && pictureFile}
            <FaImage
              className={
                "text-white h-full mx-2 w-4 transition-all duration-150 drop-shadow-glow-link-1 hover:drop-shadow-glow-link-2 hover:scale-110 active:drop-shadow-glow-link-3 active:scale-90"
              }
            />
          </label>

          <input
            required
            // ref={img}
            id="img-file"
            onChange={uploadToClient}
            accept="image/*"
            type="file"
            className="hidden"
          />
          {createObjectURL && (
            <div className="etelaat">
              <div className="item img">
                <img src={createObjectURL} alt="user img" />
              </div>
            </div>
          )}

          <button type="submit">Sabte naam</button>
        </form>
      )}

      {sabtnaam && (
        <div className="etelaat">
          <div className="two">
            <div className="item"> First Name: {firstName.current?.value}</div>
            <div className="item"> Last Name: {lastName.current?.value}</div>
          </div>

          <div className="two">
            <div className="item">Father Name: {fatherName.current?.value}</div>
            <div className="item">
              Mahal Tavalod: {mahalTavalod.current?.value}
            </div>
          </div>

          <div className="two">
            <div className="item">
              Shomare Shenasname: {shShenasname.current?.value}
            </div>
            <div className="item"> Shomare Melli: {shMelli.current?.value}</div>
          </div>

          <div className="item"> Tarikh Tavalod: {tavalod.current?.value}</div>

          <div className="item"> Phone: {phone.current?.value}</div>
          <div className="item"> TelPhone: {telPhone.current?.value}</div>
          <div className="item"> Email: {email.current?.value}</div>
          <div className="item img">
            Image: <img src={createObjectURL} alt="user img" />
          </div>
        </div>
      )}
      <div className="links">
        <Link href={"/"} className="link" style={{ color: "white" }}>
          Back To Main Menu
        </Link>
      </div>
    </div>
  );
}
