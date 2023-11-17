using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Media;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace TTSChess
{
    
    public partial class Form1 : Form
    {
        //------------------------>#################<------> change this to your sounds locations <----------------------//
        public string SOUNDS_DIR = @"c:\SOUNDS_DIR\"; // --- + \cells ,  + \colors ,  + \pieces   ------- + \   *.wav ---//
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label10_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }

        private void splitContainer1_SplitterMoved(object sender, SplitterEventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            var myBtn = sender as Button;
            string myTags = myBtn.Tag.ToString();
            var path = "";


            string[] arrTags = myTags.ToUpper().Split(' ');   // create Arr(string) from tags(btn)
            char[] arrCell = arrTags[0].ToCharArray();        // get (word, number) of cell     type:Arr(char)

            //if btn is not empty then we go play pieces and colors sounds
            if (arrTags.Length == 3)
            {
                path = SOUNDS_DIR + @"pieces\" + arrTags[2] + ".wav";
                using (var soundPlayer = new SoundPlayer(path))
                {
                    soundPlayer.Play(); 
                }

                // 1.5s sleep
                System.Threading.Thread.Sleep(1500);
                path = SOUNDS_DIR + @"colors\" + arrTags[1] + ".wav";
                using (var soundPlayer = new SoundPlayer(path))
                {
                    soundPlayer.Play(); 
                }

                // 1.5s sleep
                System.Threading.Thread.Sleep(1500);
            }

            //playing cells sounds
            path = SOUNDS_DIR+@"cells\" + arrCell[0] + ".wav";
            using (var soundPlayer = new SoundPlayer(path))
            {
                soundPlayer.Play(); 
            }

            // 1.5s sleep
            System.Threading.Thread.Sleep(1500);
            path = SOUNDS_DIR + @"cells\" + arrCell[1] + ".wav";
            using (var soundPlayer = new SoundPlayer(path))
            {
                soundPlayer.Play(); 
            }

            
        }
    }
}
