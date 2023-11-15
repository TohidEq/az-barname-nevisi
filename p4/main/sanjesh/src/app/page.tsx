import Link from "next/link";

export default function Home() {
  return (
    <div className="home page">
      <h1>- Menu -</h1>
      <div className="links">
        <Link href={"/"}>Aazmoone sarasari</Link>
        <Link href={"/"}>Aazmoone kaardaani be kaarshenasi</Link>
        <Link href={"/"}>Aazmoone beynol melali</Link>
        <Link href={"/aazmon-khaas"}>Aazmoone khaas</Link>
      </div>
    </div>
  );
}
