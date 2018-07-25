Vue.component('grid', {
    template: `
<div class="row">
  <div class="col s12">
    <div class="card">
      <div class="card-title">Selecione o tamanho:</div>
      <div class="card-content">
        <div class="row">
          <div class="input-field col s3">
            <input placeholder="Largura" id="largura" type="text" class="validate" v-model="opt.sizeX">
            <label for="largura">Largura</label>
          </div>
          <div class="input-field col s3">
            <input placeholder="Altura" id="altura" type="text" class="validate" v-model="opt.sizeY">
            <label for="altura">Altura</label>
          </div>
          <div class="input-field col s12">
            <a class="waves-effect waves-light btn" v-on:click="gerarGrid()">gerar grid</a>
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
		sizeX: 3,
		sizeY: 3,
		boxSizeW: 25,
		boxSizeH: 25
	    },
	    gridData: [
		[] = '0'
	    ],
	    scale: {
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
		'10': 'green darken-4'
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
	    	    
	    for (let x = 0; x < this.opt.sizeX; x++) {
		grid[x] = [];
		for (let y = 0; y < this.opt.sizeY; y++) {	 
		    grid[x][y] = 0;
		}
	    }
	    
	    return grid;
	}
    }
})
