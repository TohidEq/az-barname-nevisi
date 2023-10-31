"use client";
export default function Home() {
  return (
    <main className="blog page ">
      <article className="blog-post ">
        <div className="post-title ">
          <h1 className=" drop-shadow-glow">Main App</h1>
          <span>
            Lotfan maghaadire khaaste shode raa be dorosti vaared konid!(faghat
            adaad)
          </span>
        </div>

        <section className="post-section">
          <form action="" autoComplete="flase" className="f-form">
            <input
              type="text"
              name="i-tel"
              className="my-i i-tel"
              placeholder="Shomareye shoma..."
            />
            <input
              type="text"
              name="i-mokaleme"
              className="my-i i-mokaleme"
              placeholder="Mokaleme(min)"
            />
            <input
              type="text"
              name="i-internet"
              className="my-i i-internet"
              placeholder="Internet(min)"
            />
            <input
              type="text"
              name="i-payamsoti"
              className="my-i i-payamsoti"
              placeholder="Payam soti(tedaad)"
            />
            <input
              type="text"
              name="i-payamak"
              className="my-i i-payamak"
              placeholder="Payamak(tedaad)"
            />

            <button type="submit" className="my-i">
              Submit
            </button>
          </form>
        </section>

        <section className="post-section">
          <h2 className=" drop-shadow-glow">Natije</h2>
          <span>test text</span>
        </section>
      </article>
    </main>
  );
}
