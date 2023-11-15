"use client";
import { useRef } from "react";
import TextareaAutosize from "react-textarea-autosize";

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
  const img = useRef<HTMLInputElement>(null);

  return (
    <div className="page form-section">
      <h2>Aazmoone khaas</h2>
      <form action="" className="my-form" autoComplete="off">
        <div className="two">
          <input
            ref={firstName}
            className="input"
            type="text"
            id="first-name"
            placeholder="Naam"
          />
          <input
            ref={lastName}
            className="input"
            type="text"
            id="last-name"
            placeholder="Naam khaanevadegi"
          />
        </div>
        <div className="two">
          <input
            ref={fatherName}
            className="input"
            type="text"
            id="father-name"
            placeholder="Naam pedar"
          />
          <input
            ref={mahalTavalod}
            className="input"
            type="text"
            id="mahal-tavalod"
            placeholder="Mahal tavalod"
          />
        </div>

        <div className="two">
          <input
            ref={shShenasname}
            className="input"
            type="text"
            id="sh-shenasname"
            placeholder="Shomare Shenasname"
          />
          <input
            ref={shMelli}
            className="input"
            type="text"
            id="sh-melli"
            placeholder="Shomare melli"
          />
        </div>

        <span>Taarikh tavalod:</span>
        <input
          ref={tavalod}
          className="input"
          type="date"
          name=""
          id="tavalod"
        />

        <TextareaAutosize
          ref={address}
          className="input"
          required
          minRows={3}
          autoComplete="off"
          // ref={blogText}
          id="text"
          placeholder="Address"
          // disabled={disableForm}
        />
        <input
          ref={phone}
          className="input"
          type="text"
          id="phone"
          placeholder="Phone"
        />
        <input
          ref={telPhone}
          className="input"
          type="text"
          id="telphone"
          placeholder="Telephone hamraah"
        />

        <input
          ref={email}
          className="input"
          type="email"
          name=""
          id="email"
          placeholder="Email"
        />
        <span>Aks:</span>
        <input
          ref={img}
          className="input"
          type="file"
          src=""
          alt=""
          id="img-file"
        />

        <button type="submit">Sabte naam</button>
      </form>
    </div>
  );
}
