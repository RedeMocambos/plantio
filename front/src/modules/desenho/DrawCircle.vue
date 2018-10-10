<template>
<div class="row">
  <div class="col s12">
    <div class="card">
      <div class="card-title">Selecione o tamanho:</div>
      <div class="card-content">
        <div class="row">
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
        </div>
        <div class="row">
          <div class="input-field col s2">
            <a class="waves-effect waves-light btn-small" v-on:click="drawCircle()">gerar circulo</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>
<script>
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'DrawCircle',
    props: {
        gridData: null,
        scale: null,
        opt: null
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
        },
    },
    created: function() {
        this.localGridData = this.gridData;
    },
    methods: {
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
        },
    },
  };
</script>
