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
          <div class="input-field col s2">
            <p>
              <label for="range">Raio</label>
              <input
                type="range"
                id="range"
                min="1"
                name="range"
                :max="circleMaxSize"
                v-model="opt.range"
                />
            </p>
          </div>
          <div class="input-field col s2">
            <p>
              <label for="density">Densidade da copa</label>
              <input
                type="range"
                id="density"
                min="1"
                name="density"
                :max="opt.densityMax"
                v-model="opt.density"               
                />
            </p>
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
                range: 9,
                density: 2,
                densityMax: 15,
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
            let maxColorByDensity = Math.round((scaleLength * this.opt.density) / this.opt.densityMax);
            
            for (let x = 0; x < this.opt.sizeX; x++) {
                xIn = (Math.round(this.opt.sizeX /2) * -1) + x + 1;

                grid[x] = [];
                for (let y = 0; y < this.opt.sizeY; y++) {
                    yIn = (Math.round(this.opt.sizeY /2) * -1) + y + 1;

                    let color = 0;
                    
                    if ((Math.abs(yIn) ** 2) + Math.abs(xIn ** 2) < (this.opt.range ** 2)) {
                        let hypo = (Math.sqrt(Math.abs(yIn ** 2) + Math.abs(xIn ** 2)));
                        color = Math.floor((this.opt.range - hypo) * (this.opt.density / (4)));
                    }
                    
                    if (color > maxColorByDensity) {
                        color = maxColorByDensity;
                    }
                    grid[x][y] = {
                        'x': xIn,
                        'y': yIn,
                        'value': color
                    }
                }
            }
            return grid;
        },

        drawCircle: function() {

            this.opt.range = parseInt(this.opt.range);
            this.opt.sizeX = parseInt(this.opt.sizeX);
            
            let range = this.opt.range;
            
            if (range >= (this.opt.sizeX / 2)) {
                range = parseInt((this.opt.sizeX / 2)) - 1;
                this.opt.range = range;
             }
            
            // Para fazer elipses, modular rangeX e rangeY. Para circulo perfeito, = range
            let rangeX = range;
            let rangeY = range;
            
            let gridCircle = this.gridData;
            

            // Midpoint circle algorithm
            // https://rosettacode.org/wiki/Bitmap/Midpoint_circle_algorithm
            
            let f = 1 - range;
            let ddf_x = 1
            let ddf_y = -2 * range;
            let x = 0;
            let y = range;
            let color = 4;
            
            gridCircle[rangeX][rangeY + range].value = color;
            gridCircle[rangeX][rangeY - range].value = color;
            gridCircle[rangeX + range][rangeY].value = color;
            gridCircle[rangeX - range][rangeY].value = color;

            while (x < y) {
                if (f >= 0) {
                    y -= 1;
                    ddf_y += 2;
                    f += ddf_y;
                }
                x += 1;
                ddf_x += 2;
                f += ddf_x;
                
                gridCircle[rangeX + x][rangeY + y].value = color;
                gridCircle[rangeX - x][rangeY + y].value = color;
                gridCircle[rangeX + x][rangeY - y].value = color;
                gridCircle[rangeX - x][rangeY - y].value = color;
                gridCircle[rangeX + y][rangeY + x].value = color;
                gridCircle[rangeX - y][rangeY + x].value = color;
                gridCircle[rangeX + y][rangeY - x].value = color;
                gridCircle[rangeX - y][rangeY - x].value = color;
            }
            
            this.gridData  = gridCircle;            
        }
    },
    computed: {
        circleMaxSize: function() {
            return this.opt.sizeX / 2;
        }
    }
})
