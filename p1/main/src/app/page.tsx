"use client";
import { useRef, useState } from "react";
import { BiSolidError } from "react-icons/bi";
export default function Home() {
  const validate = new RegExp("[0-9]{1,20}$");
  const phone = useRef<HTMLInputElement>(null);
  const mokaleme = useRef<HTMLInputElement>(null);
  const internet = useRef<HTMLInputElement>(null);
  const payamsoti = useRef<HTMLInputElement>(null);
  const payamak = useRef<HTMLInputElement>(null);

  const [phoneError, setPhoneError] = useState<boolean>(false);
  const [mokalemeError, setMokalemeError] = useState<boolean>(false);
  const [internetError, setInternetError] = useState<boolean>(false);
  const [payamsotiError, setPayamsotiError] = useState<boolean>(false);
  const [payamakError, setPayamakError] = useState<boolean>(false);

  const [natije, setNatije] = useState<boolean>(false);
  const [hzine, setHzine] = useState<number>(0);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    setNatije(false);
    setPhoneError(!validate.test(phone.current?.value!));
    setMokalemeError(!validate.test(mokaleme.current?.value!));
    setInternetError(!validate.test(internet.current?.value!));
    setPayamsotiError(!validate.test(payamsoti.current?.value!));
    setPayamakError(!validate.test(payamak.current?.value!));

    if (
      !(
        phoneError ||
        mokalemeError ||
        internetError ||
        payamsotiError ||
        payamakError
      )
    ) {
      setHzine(
        parseInt(mokaleme.current?.value!) * 10 +
          parseInt(internet.current?.value!) * 18 +
          parseInt(payamsoti.current?.value!) * 5 +
          parseInt(payamak.current?.value!) * 5 +
          150
      );
      setNatije(true);
    }
  };

  return (
    <main className="blog page ">
      <article className="blog-post ">
        <div className="post-title ">
          <h1 className=" drop-shadow-glow">Main App</h1>
          <span>
            Lotfan maghaadire khaaste shode raa be dorosti vaared konid! (faghat
            adaad)
          </span>
        </div>

        <section className="post-section">
          <form
            action=""
            autoComplete="flase"
            className="f-form"
            onSubmit={handleSubmit}
          >
            {phoneError && (
              <span>
                <BiSolidError />
                lotfan meghdar adadi vaared konid
              </span>
            )}
            <input
              required
              type="text"
              name="i-tel"
              className="my-i i-tel"
              placeholder="Shomareye shoma..."
              ref={phone}
            />
            {mokalemeError && (
              <span>
                <BiSolidError />
                lotfan meghdar adadi vaared konid
              </span>
            )}
            <input
              required
              type="text"
              name="i-mokaleme"
              className="my-i i-mokaleme"
              placeholder="Mokaleme(min)"
              ref={mokaleme}
            />
            {internetError && (
              <span>
                <BiSolidError />
                lotfan meghdar adadi vaared konid
              </span>
            )}
            <input
              required
              type="text"
              name="i-internet"
              className="my-i i-internet"
              placeholder="Internet(min)"
              ref={internet}
            />
            {payamsotiError && (
              <span>
                <BiSolidError />
                lotfan meghdar adadi vaared konid
              </span>
            )}
            <input
              required
              type="text"
              name="i-payamsoti"
              className="my-i i-payamsoti"
              placeholder="Payam soti(tedaad)"
              ref={payamsoti}
            />
            {payamakError && (
              <span>
                <BiSolidError />
                lotfan meghdar adadi vaared konid
              </span>
            )}
            <input
              required
              type="text"
              name="i-payamak"
              className="my-i i-payamak"
              placeholder="Payamak(tedaad)"
              ref={payamak}
            />

            <button type="submit" className="my-i">
              Submit
            </button>
          </form>
        </section>

        <section className="post-section">
          <h2 className=" drop-shadow-glow">Natije</h2>
          {natije && (
            <div className="natije">
              <p>
                Shomare:{" "}
                <span className="drop-shadow-glow-link-1">
                  {phone.current?.value!}
                </span>
              </p>
              <p>
                Hazine: <span className="drop-shadow-glow-link-1">{hzine}</span>{" "}
                Tumaan
              </p>
            </div>
          )}
        </section>
      </article>
    </main>
  );
}
