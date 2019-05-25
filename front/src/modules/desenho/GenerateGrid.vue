<template>
    <div class="row">
        <div class="input-field col s2">
            <a
                class="waves-effect waves-light btn-small"
                @click="parseGrid()"
            >gerar desenho</a>
        </div>

        <div class="input-field col s12">
            <GridItens
                :opt="opt"
                :scale="scale"
                :grid-data="localData"/>
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
    props: {
        scale: null,
        opt: null,
    },
    data() {
        return {
            localData: [
                [] = '0',
            ],
            localOpt: {},
        };
    },
    mounted() {
        this.localOpt = this.opt;
    },
    methods: {
        ...mapActions({
            defineGridData: 'desenho/defineGridData',
        }),
        parseGrid() {
            this.localData = this.generateGrid();
        },
        generateGrid() {
            if (typeof this.opt.sizeX === null ||
                typeof this.opt.sizeY === null
            ) {
                return;
            }

            const grid = [];
            this.localOpt.sizeX = parseInt(this.localOpt.sizeX);
            this.localOpt.sizeY = parseInt(this.localOpt.sizeY);

            let xIn,
                yIn = 0;
            const scaleLength = Object.keys(this.scale).length - 2;
            const maxColorByDensity = Math.round((scaleLength * this.localOpt.density) / this.localOpt.densityMax);

            for (let x = 0; x < this.localOpt.sizeX; x++) {
                xIn = (Math.round(this.localOpt.sizeX / 2) * -1) + x + 1;

                grid[x] = [];
                for (let y = 0; y < this.localOpt.sizeY; y++) {
                    yIn = (Math.round(this.localOpt.sizeY / 2) * -1) + y + 1;

                    const color = 0;

                    grid[x][y] = {
                        x: xIn,
                        y: yIn,
                        value: color,
                    };
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
            ) {
                this.parseGrid();
            }
        },
    },
};
</script>
