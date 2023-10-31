import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        white: "#D3D5FD",
        light: "#929AAB",
        dark: "#474A56",
        black: "#0B0B0D",
      },
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      dropShadow: {
        glow: ["0px 0px 8px #D3D5FD"],
        glow2: ["0px 0px 8px #D3D5FD", "0px 0px 8px #D3D5FD"],
        "glow-link-1": ["0px 0px 9px #D3D5FD"],
        "glow-link-2": ["0px 0px 9px #D3D5FD", "0px 0px 9px #D3D5FD"],
        "glow-link-3": ["0px 0px 8px #D3D5FD", "0px 0px 8px #D3D5FD"],
      },
    },
  },
  plugins: [require("@tailwindcss/typography")],
};
export default config;
