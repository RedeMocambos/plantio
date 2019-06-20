<template>
    <v-container
        fluid
    >
        <v-layout>
            <v-flex v-if="dadosEspecie.id === 'undefined'">
                <carregando
                    :text="'Carregando dados da edição'"
                />
            </v-flex>
            <v-flex
                v-else
                xs10
                offset-xs1
            >
                <v-form
                    v-model="valid"
                >
                    <v-card
                        class="pl-3"
                    >
                        <v-card-title>
                            <div class="headline">
                                Edição de espécie
                            </div>
                        </v-card-title>
                        <v-text-field
                            v-model="dadosEspecie.familia"
                            label="Família"
                            @change="atualizarCampo('familia', $event) "
                        />
                        <v-text-field
                            v-model="dadosEspecie.nome_cientifico"
                            label="Nome científico"
                            @change="atualizarCampo('nome_cientifico', $event) "
                        />
                        <v-text-field
                            v-model="dadosEspecie.nomes_populares"
                            label="Nomes populares"
                            @change="atualizarCampo('nomes_populares', $event) "
                        />
                    </v-card>
                    <v-card
                        class="pa-3"
                    >
                        <v-text-field
                            v-model="dadosEspecie.inicio_colheita"
                            label="Início da colheita"
                            @change="atualizarCampo('inicio_colheita', $event) "
                        />
                        <v-select
                            v-model="dadosEspecie.porte"
                            :items="getEspecieMetadata.porte"
                            item-text="descricao"
                            item-value="valor"
                            label="Porte"
                            @change="atualizarCampo('porte', $event) "
                        />
                        <v-select
                            v-model="dadosEspecie.estrato"
                            :items="getEspecieMetadata.estrato"
                            item-text="descricao"
                            item-value="valor"
                            label="Estrato"
                            @change="atualizarCampo('estrato', $event) "
                        />
                        <v-select
                            v-model="dadosEspecie.sucessao"
                            :items="getEspecieMetadata.sucessao"
                            item-text="descricao"
                            item-value="valor"
                            label="Sucessão"
                            @change="atualizarCampo('sucessao', $event) "
                        />
                        <v-select
                            v-model="dadosEspecie.umidade"
                            :items="getEspecieMetadata.umidade"
                            item-text="descricao"
                            item-value="valor"
                            label="Umidade"
                            @change="atualizarCampo('umidade', $event) "
                        />
                        <v-select
                            v-model="dadosEspecie.tolerancia_poda"
                            :items="rangePoda"
                            label="Tolerância a poda"
                            @change="atualizarCampo('tolerancia_poda', $event) "
                        />
                    </v-card>
                    <v-card
                        class="pa-3"
                    >
                        <v-text-field
                            v-model="dadosEspecie.temperatura_min"
                            xs4
                            label="Temperatura mínima"
                            @change="atualizarCampo('temperatura_min', $event) "
                        />
                        <v-text-field
                            v-model="dadosEspecie.temperatura_max"
                            xs4
                            label="Temperatura máxima"
                            @change="atualizarCampo('temperatura_max', $event) "
                        />
                    </v-card>
                    <v-btn
                        color="info"
                        @click="salvar()"
                    >
                        <v-icon
                            class="pr-3"
                        >save</v-icon>
                        salvar
                    </v-btn>
                    <v-btn
                        color="error"
                        @click="voltar()"
                    >
                        <v-icon
                            class="pr-3"
                        >cancel</v-icon>
                        cancelar
                    </v-btn>
                </v-form>
            </v-flex>
        </v-layout>
    </v-container>
</template>
<script>
import Carregando from '@/components/CarregandoVuetify';
import Tools from '@/mixins/tools';
import { mapActions, mapGetters } from 'vuex';

export default {
    name: 'EditarEspecie',
    components: {
        Carregando,
    },
    mixins: [
        Tools,
    ],
    data() {
        return {
            valid: true,
            dadosEditados: {
                id: '',
                nomes_populares: '',
                nome_cientifico: '',
                familia: '',
                exigencia_solo: '',
                temperatura_min: '',
                temperatura_max: '',
                inicio_colheita: '',
                tempo_vida: '',
                sucessao: '',
                porte: '',
                umidade: '',
                tolerancia_poda: '',
            },
            rangePoda: [
                ...Array(10).keys(),
            ],
        };
    },
    computed: {
        ...mapGetters({
            dadosEspecie: 'especie/especie',
            getEspecieMetadata: 'especie/getEspecieMetadata',
        }),
        id() {
            return this.$route.params.id;
        },
    },
    watch: {
        dadosEspecie() {
            this.inicializarDadosEspecie();
        },
    },
    created() {
        if (typeof this.$route.params.id !== 'undefined') {
            this.buscarEspecie(this.$route.params.id);
            this.buscarEspecieMetadata();
        }
    },
    methods: {
        ...mapActions({
            buscarEspecie: 'especie/buscarEspecie',
            buscarEspecieMetadata: 'especie/buscarEspecieMetadata',
            updateEspecie: 'especie/updateEspecie',
        }),
        inicializarDadosEspecie() {
            this.dadosEditados = {
                id: this.dadosEspecie.id,
                nomes_populares: this.dadosEspecie.nomes_populares,
                nome_cientifico: this.dadosEspecie.nome_cientifico,
                familia: this.dadosEspecie.familia,
                exigencia_solo: this.dadosEspecie.exigencia_solo,
                temperatura_min: this.dadosEspecie.temperatura_min,
                temperatura_max: this.dadosEspecie.temperatura_max,
                inicio_colheita: this.dadosEspecie.inicio_colheita,
                tempo_vida: this.dadosEspecie.tempo_vida,
                sucessao: this.dadosEspecie.sucessao,
                porte: this.dadosEspecie.porte,
                tolerancia_poda: this.dadosEspecie.tolerancia_poda,
            };
        },
        atualizarCampo(key, value) {
            if (Object.keys(this.dadosEditados).includes(key)) {
                this.dadosEditados[key] = value;
            }
        },
        salvar() {
            this.updateEspecie(this.dadosEditados);
        },
    },
};
</script>
