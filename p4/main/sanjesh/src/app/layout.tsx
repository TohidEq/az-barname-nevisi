import "@/styles/index.scss";

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Sanjesh",
  description: "Site sanjeshe testie daaneshgaah",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body>
        <div className="app">{children}</div>
      </body>
    </html>
  );
}
