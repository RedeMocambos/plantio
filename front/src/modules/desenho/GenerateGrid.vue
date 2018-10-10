<template>
<div class="row">
  <div class="input-field col s2">
    <a class="waves-effect waves-light btn-small" v-on:click="parseGrid()">gerar desenho</a>
  </div>
  
  <div class="input-field col s12">
    <GridItens
      :opt="opt"
      :scale="scale"
      :grid-data="localData">
    </GridItens>
  </div>
</div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';
import GridItens from './GridItens';

export default {
    name: '',
    components: {
        GridItens,
    },
    data: function() {
        return {
            localData: [
                [] = '0'
            ],
            localOpt: {},
        };
    },
    props: {
        scale: null,
        opt: null,
    },    
    mounted() {
        this.localOpt = this.opt;
    },
    methods: {
        ...mapActions({
            defineGridData: 'desenho/defineGridData',
        }),
        parseGrid: function() {
            this.localData = this.generateGrid();
        },        
        generateGrid: function() {
            if (typeof this.opt.sizeX === null ||
                typeof this.opt.sizeY === null
               ) {
                return;
            }
            
            let grid = [];
            this.localOpt.sizeX = parseInt(this.localOpt.sizeX);
            this.localOpt.sizeY = parseInt(this.localOpt.sizeY); 
            
            let xIn, yIn = 0;
            let scaleLength = Object.keys(this.scale).length - 2;
            let maxColorByDensity = Math.round((scaleLength * this.localOpt.density) / this.localOpt.densityMax);
            
            for (let x = 0; x < this.localOpt.sizeX; x++) {
                xIn = (Math.round(this.localOpt.sizeX /2) * -1) + x + 1;

                grid[x] = [];
                for (let y = 0; y < this.localOpt.sizeY; y++) {
                    yIn = (Math.round(this.localOpt.sizeY /2) * -1) + y + 1;

                    let color = 0;
                    
                    grid[x][y] = {
                        'x': xIn,
                        'y': yIn,
                        'value': color
                    }
                }
            }
            return grid;
        },
    },
    watch: {
        localOpt() {
            console.log(this.localOpt.sizeX);
            if (this.localOpt.sizeX !== null &&
                this.localOpt.sizeY !== null
               )
            {
                this.parseGrid();
            }
        },
    }
}
</script>
