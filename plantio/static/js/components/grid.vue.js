Vue.component('grid', {
    template: `
<div class="row">
  <div class="col s12">
    <div class="card">
      <div class="card-title">Selecione o tamanho:</div>
      <div class="card-content">
        <div class="row">
          <div class="input-field col s1">
            <input placeholder="Altura" id="largura" type="text" class="validate" v-model="opt.sizeX">
            <label for="largura">Altura</label>
          </div>
          <div class="input-field col s1">
            <input placeholder="Largura" id="altura" type="text" class="validate" v-model="opt.sizeY">
            <label for="altura">Largura</label>
          </div>
          <div class="input-field col s1">
            <input placeholder="Raio" id="raio" type="text" class="validate" v-model="opt.raio">
            <label for="raio">Raio</label>
          </div>
        </div>
        <div class="row">
          <div class="input-field col s2">
            <a class="waves-effect waves-light btn-small" v-on:click="gerarGrid()">gerar grid</a>
          </div>
          <div class="input-field col s2">
            <a class="waves-effect waves-light btn-small" v-on:click="drawCircle()">gerar circulo</a>
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="col s12" v-if="iniciado">
    <div class="card">
      <div id="grid" style="font-family: monospace">
        <grid-itens
          :opt="opt"
          :scale="scale"
          :grid-data="gridData">
        </grid-itens>
      </div>
    </div>
  </div>
</div>
`,
    props: {
    },
    data: function() {
        return {
            opt: {
                sizeX: 20,
                sizeY: 20,
                boxSizeW: 20,
                boxSizeH: 20,
                raio: 9,
            },
            gridData: [
                [] = '0'
            ],
            scale: {
                '-1': 'grey lighten-3',
                '0': '',
                '1': 'light-green lighten-4',
                '2': 'light-green lighten-3',
                '3': 'green lighten-3',
                '4': 'green lighten-2',
                '5': 'green lighten-1',
                '6': 'green',
                '7': 'green darken-1',
                '8': 'green darken-2',
                '9': 'green darken-3',
                '10': 'green darken-4',
            },
            iniciado: false,
            output: ''
        }
    },    
    created: function() {
    },
    methods: {
        gerarGrid: function() {
            if (this.opt.sizeX != '' && this.opt.sizeY != '') {
                this.gridData = this.generateGrid();
                this.iniciado = true;
            }
        },
        
        generateGrid: function() {
            let grid = [];
            this.opt.sizeX = parseInt(this.opt.sizeX);
            this.opt.sizeY = parseInt(this.opt.sizeY); 
            
            let xIn, xY = 0;
            let scaleLength = Object.keys(this.scale).length - 2;
            
            for (let x = 0; x < this.opt.sizeX; x++) {
                xIn = (Math.round(this.opt.sizeX /2) * -1) + x + 1;

                grid[x] = [];
                for (let y = 0; y < this.opt.sizeY; y++) {
                    yIn = (Math.round(this.opt.sizeY /2) * -1) + y + 1;

                    let cor = 0;
                    
                    if ((Math.abs(yIn) ** 2) + Math.abs(xIn ** 2) < (this.opt.raio ** 2)) {
                        let hypo = parseInt(Math.sqrt(Math.abs(yIn ** 2) + Math.abs(xIn ** 2)));
                        cor = this.opt.raio - hypo;
                    }
                    
                    if (cor > scaleLength) {
                        cor = 10;
                    }
                    grid[x][y] = {
                        'x': xIn,
                        'y': yIn,
                        'value': cor
                    }
                }
            }
            return grid;
        },

        drawCircle: function() {

            this.opt.raio = parseInt(this.opt.raio);
            this.opt.sizeX = parseInt(this.opt.sizeX);
            
            let raio = this.opt.raio;
            
            if (raio >= (this.opt.sizeX / 2)) {
                raio = parseInt((this.opt.sizeX / 2)) - 1;
                this.opt.raio = raio;
             }
            
            // Para fazer elipses, modular raioX e raioY. Para circulo perfeito, = raio
            let raioX = raio;
            let raioY = raio;
            
            let gridCircle = this.gridData;
            

            // Midpoint circle algorithm
            // https://rosettacode.org/wiki/Bitmap/Midpoint_circle_algorithm
            
            let f = 1 - raio;
            let ddf_x = 1
            let ddf_y = -2 * raio;
            let x = 0;
            let y = raio;
            let cor = 4;
            
            gridCircle[raioX][raioY + raio].value = cor;
            gridCircle[raioX][raioY - raio].value = cor;
            gridCircle[raioX + raio][raioY].value = cor;
            gridCircle[raioX - raio][raioY].value = cor;

            while (x < y) {
                if (f >= 0) {
                    y -= 1;
                    ddf_y += 2;
                    f += ddf_y;
                }
                x += 1;
                ddf_x += 2;
                f += ddf_x;
                
                gridCircle[raioX + x][raioY + y].value = cor;
                gridCircle[raioX - x][raioY + y].value = cor;
                gridCircle[raioX + x][raioY - y].value = cor;
                gridCircle[raioX - x][raioY - y].value = cor;
                gridCircle[raioX + y][raioY + x].value = cor;
                gridCircle[raioX - y][raioY + x].value = cor;
                gridCircle[raioX + y][raioY - x].value = cor;
                gridCircle[raioX - y][raioY - x].value = cor;
            }
            
            this.gridData  = gridCircle;            
        }
    }
})
