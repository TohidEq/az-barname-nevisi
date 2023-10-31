import type { Metadata } from "next";

import "@/styles/index.scss";

export const metadata: Metadata = {
  title: "Main App",
  description: "Barnameye mohasebeye hazineye telephone hamraah",
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
